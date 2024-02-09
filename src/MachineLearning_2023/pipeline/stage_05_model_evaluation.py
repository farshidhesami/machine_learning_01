from MachineLearning_2023.config.configurations import ConfigurationManager
from MachineLearning_2023.components.model_evaluation import ModelEvaluation
from MachineLearning_2023 import logger
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

STAGE_NAME = "Model evaluation stage"

# Define the model evaluation functions
def evaluate_logistic_regression(X_train, y_train, X_test, y_test):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    confusion_mat = confusion_matrix(y_test, y_pred)
    
    return accuracy, confusion_mat

def evaluate_extra_trees_classifier(X_train, y_train, X_test, y_test):
    classifier = ExtraTreesClassifier()
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    confusion_mat = confusion_matrix(y_test, y_pred)
    
    return accuracy, confusion_mat

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        self.config_manager = ConfigurationManager()

    def main(self):
        model_evaluation_config = self.config_manager.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.save_results()

        # Load your dataset
        DATA_PATH = 'data/winequality-red.csv'
        wines = pd.read_csv(DATA_PATH)

        # Assuming 'quality' is the target variable
        X = wines.drop('quality', axis=1)
        y = wines['quality']

        # Splitting the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

        # Evaluate Logistic Regression
        logistic_accuracy, logistic_confusion_mat = evaluate_logistic_regression(X_train, y_train, X_test, y_test)
        print("Logistic Regression Accuracy:", logistic_accuracy)
        print("Logistic Regression Confusion Matrix:\n", logistic_confusion_mat)

        # Evaluate Extra Trees Classifier
        et_accuracy, et_confusion_mat = evaluate_extra_trees_classifier(X_train, y_train, X_test, y_test)
        print("Extra Trees Classifier Accuracy:", et_accuracy)
        print("Extra Trees Classifier Confusion Matrix:\n", et_confusion_mat)

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = ModelEvaluationTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
