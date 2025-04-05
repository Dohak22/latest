# Use a base image with Python installed
FROM python:3.10-slim

# Set the working directory to /app inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Expose the port the app will run on
EXPOSE 4000

# Set the entry point to run the Flask app
CMD ["python", "app.py"]
