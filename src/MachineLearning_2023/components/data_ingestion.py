import os
import urllib.request as request
import zipfile
from MachineLearning_2023 import logger
from MachineLearning_2023.utils.common import get_size

# Path: src/MachineLearning_2023/components/data_ingestion.py
from MachineLearning_2023.entity.config_entity import DataIngestionConfig
# Path: src/MachineLearning_2023/utils/common.py
from pathlib import Path


# Class for downloading and extracting a data file from a URL (data ingestion)
# DataIngestion class to download and extract the data from the source URL
class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    # Method to downloads a file from a URL and saves it locally under a specific directory.
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")


    # Method to extracts the downloaded zip file into a specified directory (data ingestion)
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
