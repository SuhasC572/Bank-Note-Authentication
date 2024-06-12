# Dockerized Flask Machine Learning API

This comprehensive guide covers the setup and deployment of a Flask-based Machine Learning API within a Docker container. The application utilizes a pre-trained machine learning model to make predictions based on user input. It leverages Docker for easy deployment and Anaconda to manage dependencies, ensuring a consistent environment across different setups.

## Features

- **Anaconda Environment**: Uses the `continuumio/anaconda3:4.4.0` Docker image for dependency management.
- **Flask Application**: A lightweight web server to serve the Machine Learning API.
- **Machine Learning Integration**: Incorporates a pre-trained model for making predictions.
- **Docker Integration**: Simplifies deployment and ensures consistency across environments.

## Prerequisites

Before starting, ensure you have Docker installed on your system.

## Installation

To set up the project environment, follow these steps:

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Create and Activate a Virtual Environment

For Windows:

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

## Usage

To run the application:

```bash
python main_copy.py
```

After running the application, navigate to [http://localhost:5000/apidocs](http://localhost:5000/apidocs) to view the Swagger UI and interact with the API.

## Setup

### 1. Clone the Repository

Clone this repository to your local machine to get started with the Dockerized Flask application.

### 2. Build the Docker Image

Navigate to the directory containing the Dockerfile and build the Docker image:

```bash
docker build -t flask_ml_api .
```

### 3. Run the Docker Container

Run the container, mapping port 5000 of the container to port 5000 on your host:

```bash
docker run -p 5000:5000 flask_ml_api
```

This allows you to access the Flask application via [http://localhost:5000](http://localhost:5000).

## Application Structure

- **Dockerfile**: Sets up the Anaconda environment, copies application files, and specifies the command to run the Flask server.
- **main_copy.py**: Initializes the Flask app, loads the machine learning model, and defines API endpoints for predictions.
- **model/**: Contains the pre-trained machine learning model and any associated data preprocessing scripts.

## Using the Application

With the Docker container running, access the application by navigating to [http://localhost:5000](http://localhost:5000) in your web browser. The application provides endpoints for submitting data and receiving predictions from the pre-trained model. The specifics of these endpoints and their usage are detailed within `main_copy.py`.

## Machine Learning Model Integration

- **Model Loading**: Upon startup, `main_copy.py` loads the pre-trained model from the `model/` directory.
- **Prediction Endpoint**: Users submit data to a specific endpoint, which invokes the model to make a prediction and returns the result.
