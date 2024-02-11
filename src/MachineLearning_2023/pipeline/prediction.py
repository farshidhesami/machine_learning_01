import joblib
import numpy as np
import pandas as pd
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# This class is used to make predictions using the trained model
class PredictionPipeline:
    def __init__(self):
        try:
            self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))
            logging.info("Model loaded successfully.")
        except FileNotFoundError:
            logging.error("Model file not found.")
            self.model = None

    # This method is used to make predictions using the trained model
    def prediction(self, data):
        if self.model is None:
            logging.error("No model is loaded.")
            return None

        # Validate input data (this is just an example, adjust according to your needs)
        if not isinstance(data, pd.DataFrame):
            logging.error("Invalid input data type. Expected pandas DataFrame.")
            return None

        prediction = self.model.predict(data)
        return prediction
    
    
        
       # simple code for prediction without logging and error handling and debugging.
        """
import joblib 
import numpy as np
import pandas as pd
from pathlib import Path


class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    
    def predict(self, data):
        prediction = self.model.predict(data)

        return prediction
        
        """