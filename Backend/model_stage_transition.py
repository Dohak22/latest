import mlflow
from mlflow.tracking import MlflowClient

# Define model and version details
model_name = "FakeNewsModel"
model_version = 2  # The version you want to promote

# Initialize the MLflow client
client = MlflowClient()

# Promote model to Production stage
client.transition_model_version_stage(
    name=model_name,
    version=model_version,
    stage="Production"  # You can also use "Staging" or other stages
)

print(f"Model version {model_version} is now in the 'Production' stage.")
