# code from 05_model_evaluation.ipynb file in the src/MachineLearning_2023/research directory
import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, mean_squared_log_error, median_absolute_error
from urllib.parse import urlparse
import numpy as np
import joblib
# Ensure to import the ModelEvaluationConfig from the config configurations.py file
from MachineLearning_2023.entity.config_entity import ModelEvaluationConfig    
# Ensure to import the save_json from the common.py file in the src/MachineLearning_2023/utils directory 
from MachineLearning_2023.utils.common import save_json
from pathlib import Path

# for classification model evaluation
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Regression model evaluation class
class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))  # Root mean squared error 
        mae = mean_absolute_error(actual, pred)           # Mean absolute error
        r2 = r2_score(actual, pred)                       # R squared
        msle = mean_squared_log_error(actual, pred)       # Mean squared log error
        medae = median_absolute_error(actual, pred)       # Median absolute error
        return rmse, mae, r2, msle, medae

    def save_results(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        predicted_qualities = model.predict(test_x)
        
        # Unpacking the metrics directly into variables
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


    ## Classification model evaluation functions    
    
    # This function evaluates the Logistic Regression model
    def evaluate_logistic_regression(X_train, y_train, X_test, y_test):
        
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        confusion_mat = confusion_matrix(y_test, y_pred)
        
        return accuracy, confusion_mat
    
    # This function evaluates the Extra Trees Classifier model
    def evaluate_extra_trees_classifier(X_train, y_train, X_test, y_test):
        
        classifier = ExtraTreesClassifier()
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
    
        accuracy = accuracy_score(y_test, y_pred)
        confusion_mat = confusion_matrix(y_test, y_pred)
        
    
        return accuracy, confusion_mat
