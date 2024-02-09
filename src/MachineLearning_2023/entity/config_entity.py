# Config entity for data ingestion process (data ingestion config)
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)             # This code copy from 01_data_ingestion.py
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    

@dataclass(frozen=True)              # This code copy from 02_data_validation.py
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict



@dataclass(frozen=True)              # This code copy from 03_data_transformation.py
class DataTransformationConfig:
    root_dir: Path
    data_path: Path



@dataclass(frozen=True)              # This code copy from 04_data_preprocessing.py
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str




@dataclass(frozen=True)               # This code copy from 05_model_evaluation.py
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
    
    
