from MachineLearning_2023.constants import *
from MachineLearning_2023.utils.common import read_yaml, create_directories

from MachineLearning_2023.entity.config_entity import DataIngestionConfig

# Configuration Manager class to read the configuration files and return the configuration objects (data ingestion config)
class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])
        
# get_data_ingestion_config() method to return the data ingestion config object
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])
        
        # DataIngestionConfig object to be returned by the get_data_ingestion_config() method
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    
    