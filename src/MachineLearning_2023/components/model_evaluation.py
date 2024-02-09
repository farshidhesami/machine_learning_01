# code from 05_model_evaluation.ipynb file in the src/MachineLearning_2023/research directory
import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, mean_squared_log_error, median_absolute_error
from urllib.parse import urlparse
import numpy as np
import joblib
from MachineLearning_2023.entity.config_entity import ModelEvaluationConfig    # from config/configurations.py
from MachineLearning_2023.utils.common import save_json
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))  # means squared error 
        mae = mean_absolute_error(actual, pred)           # means absolute error
        r2 = r2_score(actual, pred)                       # means squared error
        msle = mean_squared_log_error(actual, pred)       # means_squared_log_error
        medae = median_absolute_error(actual, pred)       # means median_absolute_error
        return rmse, mae, r2, msle, medae
    


    def save_results(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        predicted_qualities = model.predict(test_x)

        (rmse, mae, r2, msle, medae) = self.eval_metrics(test_y, predicted_qualities)

        # Saving metrics as local
        scores = {
            "rmse": rmse,
            "mae": mae,
            "r2": r2,
            "msle": msle,
            "medae": medae
        }
        save_json(path=Path(self.config.metric_file_name), data=scores)     
