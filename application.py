from flask import Flask, render_template, request, jsonify
import subprocess
import numpy as np
import pandas as pd
from MachineLearning_2023.pipeline.prediction import PredictionPipeline 

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
            # Extracting and validating user inputs
            input_features = ['fixed_acidity', 'volatile_acidity', 'citric_acid', 'residual_sugar',
                              'chlorides', 'free_sulfur_dioxide', 'total_sulfur_dioxide', 'density',
                              'pH', 'sulphates', 'alcohol']
            data = []
            for feature in input_features:
                value = float(request.form[feature])
                data.append(value)

            data = np.array(data).reshape(1, -1)

            # Prediction
            prediction_pipeline = PredictionPipeline()
            prediction = prediction_pipeline.predict(data)

            return render_template('results.html', prediction=str(prediction))
        except Exception as e:
            return jsonify({"message": "An error occurred", "error": str(e)}), 500
    else:
        return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)






