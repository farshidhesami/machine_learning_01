from flask import Flask, render_template, request, jsonify
import subprocess
import numpy as np
import pandas as pd
from MachineLearning_2023.pipeline.prediction import PredictionPipeline
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homePage():
    return render_template('index.html')

@app.route('/train', methods=['POST'])
def training():
    try:
        # Using subprocess for better handling and security
        result = subprocess.run(['python', 'main.py'], capture_output=True, text=True, check=True)
        return jsonify({"message": "Training successful!", "details": result.stdout}), 200
    except subprocess.CalledProcessError as e:
        return jsonify({"message": "Training failed", "error": e.stderr}), 500

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            # Feature names as used in the model
            input_features = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
                              'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
                              'pH', 'sulphates', 'alcohol']
            data = []
            for feature in input_features:
                form_key = feature.replace(" ", "_")              # this code replaces spaces with underscores in the feature names to match the html form input names 
                try:
                    value = float(request.form.get(form_key, 0))  # Default to 0 if key not found
                except ValueError:
                    return jsonify({"message": "Invalid input for feature: {}".format(feature)}), 400
                data.append(value)

            # Convert list to pandas DataFrame
            data_df = pd.DataFrame([data], columns=input_features)

            prediction_pipeline = PredictionPipeline()
            prediction = prediction_pipeline.prediction(data_df)  # Pass DataFrame to prediction

            return render_template('results.html', prediction=str(prediction))
        except Exception as e:
            return jsonify({"message": "An error occurred during prediction", "error": str(e)}), 500
    else:
        return render_template('index.html')
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)  # Added debug=True for development. Remove in production.
