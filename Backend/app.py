from flask import Flask, render_template, request, jsonify
import mlflow
import mlflow.sklearn
import os

# Initialize Flask with template_folder pointing to the 'frontend' folder
app = Flask(__name__, template_folder='../frontend')  # Adjust the path to your frontend folder

# MLflow setup
mlflow.set_tracking_uri("http://localhost:5000")  # Make sure MLflow tracking server is running
model_name = "FakeNewsModel"
stage = "Production"

try:
    # Load model from MLflow model registry
    model_uri = f"models:/{model_name}/{stage}"
    pipeline = mlflow.pyfunc.load_model(model_uri)
except Exception as e:
    raise RuntimeError(f"Error loading model from MLflow: {str(e)}")

@app.route("/")
def home():
    return render_template("index.html")  # This will look for index.html in ../frontend

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if "text" not in data:
        return jsonify({"error": "No text provided"}), 400
    
    try:
        # Get the prediction from the loaded model
        prediction = pipeline.predict([data["text"]])[0]

        # Optionally, save the model again if you want to log the prediction or retrain
        with mlflow.start_run():
            mlflow.sklearn.log_model(pipeline, "model", registered_model_name=model_name)

        return jsonify({"prediction": "Real" if prediction == 1 else "Fake"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
