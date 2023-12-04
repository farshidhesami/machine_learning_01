# End-to-end-ML-Project

## Workflows :

- update config.yaml
- update schema.yaml (necessary here because used for data validation component,means that the schema defined in this file is used to check the validity of data in our
project)    
- update params.yaml (necessary here because this is regression model and This file is likely used to define parameters for a regression model in our project, Normally used in an elastic model, an ElasticNet regression model or similar ).
- update the entity
- update the configuration manager in src config
- update the components
- update the pipeline (refers to updating a data processing or machine learning pipeline)
- update the main.py
- update the app.py


- 1- Create a template.py .( Run a "python template.py )
- 2- Create a requirements.txt .
- 3- Create a setup.py (Git Bash)
- 4- use a "pip freeze" command for listing all the Python packages installed in the system .(Git Bash) 
- 5- Pip install -r requirements.txt .(Git Bash) 
- 6- Add code in src/MachineLearning_2023/__ init__.py(sets up a logger for a Python package)
- 7- Add code in src/mlproject/__ init__.py(In machine learning project where logging can be crucial for debugging and tracking the execution of your code).
- 8- Add a code in main.py for make a logs folder and running_logs.log -----> Custom logging (2023-11-30 13:46:48,356: INFO: main: Welcome to our custom logging).

- 9- Add code in src/mlproject/utils/common.py .
  - read_yaml Function : 
     - Reads a YAML file and returns its contents as a ConfigBox object.The function is well-implemented  with appropriate error handling.
  - create_directories Function:
     - Creates a list of directories and the "verbose" parameter controls logging.
  - save_json Function:
     - Saves a dictionary as a JSON file.error handling and logging are implemented. Ensure that the path is a valid file path and data is serializable. 
  - load_json Function:
     - Loads a JSON file and returns its contents as a ConfigBox object.function handles errors well. It returns None in case of an exception, which is a good practice for error handling.
  - save_bin Function:
     - Saves data in binary format using joblib.function is straightforward and logs the operation. Ensure that the data is serializable by joblib.
  - load_bin Function:
     - Loads binary data from a file.Error handling is in place. Similar to load_json, it returns None in case of an error, which is good.
  - get_size Function:
     - Gets the size of a file in KB.The function correctly calculates the file size. Error handling is present, and it returns None in case of an exception.
     
  - Note : 
     - Use of ConfigBox from the box library for handling configurations is a good choice for its simplicity and dot-access to dictionary keys .

- 10- Add some python code mention in research/trials.ipynb(ConfigBox` class and ensure_annotations training).

- 11- Create a "Expriement.ipynb" : is likely a Jupyter notebook file used in the context of a Machine Learning (ML) project,use for :
     - Loading and preprocessing data.
     - Defining a model
     - Training the model on the data
     - Evaluating the model's performance
     - Tuning the model's parameters.

- 12- Download a "winequality-red.csv" file and then zip it or (https://www.kaggle.com/datasets/uciml/red-wine-quality-cortez-et-al-2009)
- 13- I uploaded in my Github path : https://github.com/farshidhesami/Branching-tutorial/blob/master/winequality-red.zip
- 14- Go to path and click in file and right click on "View raw" and copy a link address: https://github.com/farshidhesami/Branching-tutorial/raw/master/winequality-red.zip
- 15- Copy a "winequality-red.csv" file to my vscode explorer in data/winequality-red.csv .
- 16- load a data .

