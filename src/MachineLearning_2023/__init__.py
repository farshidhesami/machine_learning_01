# sets up a logger when running the package .
# This is a standard way of setting up a logger in Python.
import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_level = os.getenv('LOG_LEVEL', 'INFO').upper()             # Get log level from environment variable, default to 'INFO'
log_dir = os.getenv('LOG_DIR', 'logs')                         # getenv is a function that get the value of a named attribute of an object
logger_name = os.getenv('LOGGER_NAME', 'MachineLearning_2023') # Get log directory from environment variable, default to 'logs'

log_filepath = os.path.join(log_dir,"running_logs.log")        # Get logger name from environment variable, default to 'MachineLearning_2023'
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= getattr(logging, log_level),
    format= logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(logger_name)