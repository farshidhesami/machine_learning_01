from MachineLearning_2023.config.configurations import ConfigurationManager     # this is the config manager
from MachineLearning_2023.components.data_ingestion import DataIngestion        # This is the data ingestion class
from MachineLearning_2023 import logger                                         # This is the logger

# Get the config manager
STAGE_NAME = "Data Ingestion stage"


class DataIngestionTrainingPipeline:           # This is the data ingestion pipeline class
    def __init__(self):
        pass

# Get the logger for the data ingestion stage  
    def main(self):                            # Copy from 01_data_ingestion.ipynb pipeline class 
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


# Get the logger for the data ingestion stage 
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
