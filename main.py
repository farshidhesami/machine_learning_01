from MachineLearning_2023 import logger 

# Importing the DataIngestionTrainingPipeline class from the stage_01_data_ingestion.py file 
from MachineLearning_2023.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# Importing the DataValidationTrainingPipeline class from the stage_02_data_validation.py file
from MachineLearning_2023.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

# Importing the DataTransformationTrainingPipeline class from the stage_03_data_transformation.py file
from MachineLearning_2023.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataTransformationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
