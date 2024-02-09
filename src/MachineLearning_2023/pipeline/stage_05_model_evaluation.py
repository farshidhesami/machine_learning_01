from MachineLearning_2023.config.configurations import ConfigurationManager
from MachineLearning_2023.components.model_evaluation import ModelEvaluation
from MachineLearning_2023 import logger
import pandas as pd
from sklearn.model_selection import train_test_split

STAGE_NAME = "Model evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        self.config_manager = ConfigurationManager()
        self.model_evaluation_config = self.config_manager.get_model_evaluation_config()

    def main(self):
        # Initialize ModelEvaluation with configuration
        model_evaluator = ModelEvaluation(config=self.model_evaluation_config)
        model_evaluator.save_results()

        # Load your dataset
        DATA_PATH = 'data/winequality-red.csv'
        wines = pd.read_csv(DATA_PATH)

        # Assuming 'quality' is the target variable
        X = wines.drop('quality', axis=1)
        y = wines['quality']

        # Splitting the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

        # Evaluate Logistic Regression and Extra Trees Classifier using ModelEvaluation class
        # If these methods are defined in ModelEvaluation class, call them like this:
        # logistic_accuracy, logistic_confusion_mat = model_evaluator.evaluate_logistic_regression(X_train, y_train, X_test, y_test)
        # et_accuracy, et_confusion_mat = model_evaluator.evaluate_extra_trees_classifier(X_train, y_train, X_test, y_test)

        # Alternatively, if these methods are not in ModelEvaluation, 
        # you need to define them in this script or import them if they're defined elsewhere

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        pipeline = ModelEvaluationTrainingPipeline()
        pipeline.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
