from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd

# This is the class we created in the previous step
from MachineLearning_2023.pipeline.prediction import PredictionPipeline 

# Initialize the Flask application and the prediction pipeline
app = Flask(__name__)

@app.route('/', methods=['GET'])   # This is the home page
def homePage():
    return render_template('index.html')   # This will render the index.html template





# Run the app on localhost:8080
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)    