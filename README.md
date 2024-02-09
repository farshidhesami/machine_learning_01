# End-to-end-ML-Project

- 1- Create a template.py .( Run a "python template.py )
- 2- Create a requirements.txt .
- 3- Create a setup.py (Git Bash)
- 4- use a "pip freeze" command for listing all the Python packages installed in the system .(Git Bash) 
- 5- Pip install -r requirements.txt .(Git Bash) 

- 6- Add code in src/MachineLearning_2023/__ init__.py(sets up a logger for a Python package)
   - Note 01 : Without an __init__.py file, Python won't recognize the directory as a package.
   - Note 02 : In my case, the __init__.py file is setting up a logger that can be used throughout the
     rest of the package . 
   - Note 03 : (In machine learning project where logging can be crucial for debugging and tracking the execution of your code).

- 7- Add code in src/MachineLearning_2023/__ init__.py .

- 8- Add a code in main.py for make a logs folder and running_logs.log (from MachineLearning_2023 import logger) 
     (Gitbash-------> python main.py )

- 9- Add code in src/MachineLearning_2023/utils/common.py .
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

## Workflows :

- A- update config.yaml
- B- update schema.yaml (necessary here because used for data validation component,means that the schema defined in this file is used to check the validity of data in our
project)    
- C- update params.yaml (necessary here because this is regression model and This file is likely used to define parameters for a regression model in our project, Normally used in an elastic model, an ElasticNet regression model or similar ).
- D- update the entity
- E- update the configuration manager in src config
- F- update the components
- G- update the pipeline (refers to updating a data processing or machine learning pipeline)
- H- update the main.py
- I- update the app.py

- Note : Add a "winequality-red.csv" into the data folder . and also uploaded as zip file in "Branching-tutorial" github. 
     - https://github.com/farshidhesami/Branching-tutorial/blob/master/winequality-red.zip

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

## Wine Quality Prediction Using Machine Learning.

### Overview :
- This project applies machine learning techniques to predict the quality of wine based on its physicochemical properties. It aims to provide an objective assessment of wine quality, which is traditionally evaluated by human experts. Using a dataset that includes various chemical attributes of Portuguese "Vinho Verde" wine, the project explores how these features correlate with wine quality, defined on a scale from 0 to 10.

### Data Description :
- The dataset includes red wine samples with the following features:

    - 1- Fixed Acidity: Predominant fixed acids like tartaric, succinic, citric, and malic acids.
    - 2- Volatile Acidity: Gaseous acids present in wine, primarily acetic acid.
    - 3- Citric Acid: A weak organic acid contributing to wine's freshness and flavor.
    - 4- Residual Sugar: Sugar content remaining post fermentation.
    - 5- Chlorides: Salt content in wine.
    - 6- Free Sulfur Dioxide: SO2 level used to prevent oxidation and spoilage.
    - 7- Total Sulfur Dioxide: Total amount of free and bound SO2.
    - 8- Density: Reflecting the alcohol and sugar content.
    - 9- pH: Indicating acidity level.
    - 10-Sulfates: Sulfites added to preserve freshness.
    - 11-Alcohol: Percentage of alcohol present.

- The target variable is the Wine Quality, rated between 0 and 10.

### Objective

- The goal is to develop a machine learning model that can accurately predict the quality of wine. This serves as a tool for winemakers and consumers alike, offering an efficient, objective way to assess wine quality.
- This project aims to predict wine quality using machine learning. In addition to regression modeling, an interesting approach is to perform binary classification, categorizing wines as "good" (1) or "not good" (0) based on an arbitrary cutoff.

### Binary Classification Approach

- To perform binary classification, follow these steps:

- 1-Arbitrary Cutoff: Choose an arbitrary cutoff point for wine quality. For example, wines with a quality score of 7 or higher can be categorized as "good," while the rest are considered "not good."

- 2-Labeling: Assign labels to the dataset based on the chosen cutoff. For wines with quality scores greater than or equal to 7, assign the label "1" (good). For wines with quality scores below 7, assign the label "0" (not good).

- 3-Model Training: Train a binary classification model using the labeled dataset. Common classifiers like Logistic Regression, Random Forest, or Support Vector Machines can be used.

- 4-Model Evaluation: Evaluate the model's performance using standard classification metrics such as accuracy, precision, recall, F1-score, and ROC-AUC. This will give you insights into how well the model can distinguish between good and not good wines.

- 5-Practical Applications: The binary classification model can be valuable for wine producers and consumers. It simplifies the assessment of wine quality, making it easier for both experts and non-experts to make informed decisions.

### Note :
- There are different types of metrics for different types of machine learning tasks (classification, regression, clustering, etc.).

- These are commonly used metrics for regression tasks:
   - Root Mean Squared Error (RMSE) : 
      - This is the square root of the average of the square of all the errors. RMSE gives a relatively high weight to large errors. This means the RMSE should be more useful when large errors are particularly undesirable.
   - Mean Absolute Error (MAE) : 
      - This is the average of the absolute differences between the predicted and actual values. It gives an idea of how wrong the predictions were.
   - R-squared (R2) : 
      - This is a statistical measure that represents the goodness of fit of a regression model. A higher R-squared indicates a better fit for the model.

- 16- The purpose of add a code in Expriement.ipynb is to show a End-To-End project and how to create any pipeline and prediction pipeline and how to combine a end-to-end project .

- Note : Inside a research folder we create a "01_data_ingestion.ipynb" its first stage .

### Stage 01 Data ingestion :

- 17- How to see a dataset in URL ?
- 18- Inside a research folder add other folder "01_data_ingestion.ipynb" .
- 19- "A"- update config.yaml", Go to "config.yaml" and add a code as a "artifacts_root" and "data_ingestion" .

- 20- "B"- update schema.yaml", Go to "schema.yaml" ,Just write a something in this phase like : key : val just fill a page .

      - A schema.yaml is a YAML (YAML Ain't Markup Language) file that defines a schema for data structures or configurations. 
      - YAML is a human-readable data serialization format commonly used for configuration files, but it can also be used for other purposes like data storage or 
        inter-process communication .

   - schema.yaml can serve various purposes::
      - Data Validation: It can be used to define the expected structure of data, such as the fields present in a JSON or XML file.
      - Configuration Management: In software applications, schema.yaml can define the structure and acceptable values for configuration settings.
      - Database Schema Definition: In the context of databases, a schema.
      - API Specification: For APIs, a schema.yaml file could be used to describe the API's structure .
      - Data Interchange Formats: In contexts where data is exchanged between different systems, a schema.

- 21- "C"- update params.yaml : Just write a something in this phase like : key : val just fill a page . 

- 22- "D"- update the entity :  add code in "config.yaml" as a data_ingestion and then add code in "01_data_ingestion.ipynb".

- 23- Go to "constants" folder and inside in '__init__.py' write a code "CONFIG_FILE_PATH & PARAMS_FILE_PATH & SCHEMA_FILE_PATH ".

- 24- Continue coding in "01_data_ingestion.ipynb" add a code " from mlProject.constants import * ".
      - * means read all code in constants/__init__.py.

- 25- Continue coding in "01_data_ingestion.ipynb" update " class ConfigurationManager " and " DataIngestionConfig".

- 26- Continue coding in "01_data_ingestion.ipynb" update "components" and "pipeline".

- 27- See artifacts folder and we have a "data_ingestion and data.zip and winequality-red.csv"

- "NoteBook file finished" .

- once again see : 
    - update config.yaml
    - update schema.yaml
    - update params.yaml
    - update the entity
    - update the configuration manager in src config
    - update the components
    - update the pipeline
    - update the main.py
    - update the app.py

- 28- Go to the entity folder "config_entity.py" and add a code .  (from 01_data_ingestion.ipynb)

- 29- Go to the research/"01_data_ingestion.ipynb" and copy code from configuration manager and class ConfigurationManager into the  "src/config/configurations.py".

- 30- Go to the components and create a "data_ingestion.py" and copy components code .

- 31- Go to update a pipeline,Create a "stage_01_data_ingestion.py" in pipeline folder and add code from 
"01_data_ingestion.ipynb" for complete a pipeline .

- 32- Go to "main.py" and Importing the DataIngestionTrainingPipeline class from the stage_01_data_ingestion.py file. 

- Note : By main.py run a "pipeline" and test it possible .

- Note : for test it delete "logs and artifacts" run a command : "python main.py"

- Note (in .gitignore) : add a "artifacts/* " in file, it will instruct Git to ignore all files and directories that match the pattern artifacts/ .

### Stage 02 Data validation :

- 33- Create in research/02_data_validation.ipynb and add code .
- once again update all step  : 
    - update config.yaml
    - update schema.yaml
    - update params.yaml
    - update the entity
    - update the configuration manager in src config
    - update the components
    - update the pipeline
    - update the main.py
    - update the app.py

- 34- first update config.yaml go to config.yaml and add a code .
- 35- Add a code in "schema.yaml" .
    - Note : Using a `schema.yaml` file like yours is a best practice in data science and machine learning, helping to maintain data integrity and streamline the model development and deployment process.Since `quality` is an integer, this could be a classification or a regression problem depending on the nature of the `quality` variable (discrete classes or a continuous range).

    - Note:A schema.yaml file in a machine learning project defines the structure and data types of dataset. Ensuring that the data used in your ML project is properly structured, validated, and consistent, which is fundamental for building reliable and robust machine learning models.
    - Define Data Structure
    - Data Type Validation
    - Facilitate Data Loading and Processing
    - Enforce Consistency
    - Integration with ML Tools
    - Documentation
    - Error Handling and Debugging
    - Supports Feature Engineering

- 36- Go to 02_data_validation.ipynb and add a code from "Experiment.ipynb"

- Note : Lets update a "SRC" :
- 37- we updated all "config.yaml and schema.yaml updated and params.yaml" . 
- 38- update entity with src/MachineLearning_2023/entity/config_entity.
- 39- update configuration manager with src/MachineLearning_2023/config/configuration.py
- 40- update components with create a "data_validation.py" src/MachineLearning_2023/components/data_validation.py. 
- 41- update the pipeline with create a "stage_02_data_validation.py" 
- 42- Add code in "main.py" for "Data Validation stage" and then test it and before that delete a artifacts folder.
- 43- Run a code in GitBash-----> python main.py------> see artifacts folder.

### Stage 03 Data transformation : 
- 44- create a "03_data_transformation.ipynb" in research folder.

- once again update all step  : 
    - update config.yaml
    - update schema.yaml
    - update params.yaml
    - update the entity
    - update the configuration manager in src config
    - update the components
    - update the pipeline
    - update the main.py
    - update the app.py

- 45- first update config.yaml
- 46- inside " 03_data_transformation.ipynb " initials entity 
  47- inside " 03_data_transformation.ipynb " update the configuration manager class and "DataTransformationConfig" .
    - Note: data_transformation related to "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)" inside "Experiment.ipynb".

  48- inside " 03_data_transformation.ipynb " Import libraries .
  49- inside " 03_data_transformation.ipynb " update the components.
  50- inside " 03_data_transformation.ipynb " Update the pipeline.
  51- execute code.(inside a artifacts/data_transformation two data generated "test.csv" and "train.csv").

  52- update entity with src/MachineLearning_2023/entity/config_entity.
  53- update configuration manager with src/MachineLearning_2023/config/configuration.py
  54- update components with create a "data_transformation.py" src/MachineLearning_2023/components/data_transformation.py. 
  55- update the pipeline with create a "stage_03_data_transformation.py" .
  56- Add code in "main.py" for "data_transformation.py" and then test it and before that delete a artifacts folder.
  57-Run a code in GitBash-----> python main.py------> see artifacts folder. 

### Stage 04 Model Trainer : 

58- first update config.yaml.
59- add code in "params.yaml". (This Code related to Elastic Net Regression.Add a "params.yaml" helps to save time to change a parameter in  "components" )
  - Note : The `params.yaml` file you've described is used to configure parameters for an 
    "ElasticNet model".   

    - once again update all step  : 
    - update config.yaml
    - update schema.yaml
    - update params.yaml
    - update the entity
    - update the configuration manager in src config
    - update the components
    - update the pipeline
    - update the main.py
    - update the app.py

60- inside " 04_model_trainer.ipynb " initials entity    
61- inside " 04_model_trainer.ipynb " update the configuration manager class and "class ConfigurationManager" .
62- inside " 04_model_trainer.ipynb " Import libraries .
63- inside " 04_model_trainer.ipynb " update the components.
64- inside " 04_model_trainer.ipynb " Update the pipeline.
65- execute code. (inside a artifacts/model_trainer/model.joblib created ).

66- update entity with src/MachineLearning_2023/entity/config_entity.
67- update configuration manager with src/MachineLearning_2023/config/configuration.py
68- update components with create a "model_trainer.py" src/MachineLearning_2023/components/model_trainer.py. 
69- update the pipeline with create a "stage_04_model_trainer.py".
70- Add code in "main.py" for "Model Trainer stage" and then test it and before that delete a artifacts folder.
71-Run a code in GitBash-----> python main.py------> see artifacts folder. 


### Stage 05 Model evaluation : 

72- Create a ( 05_model_evaluation.ipynb ) and then first update config.yaml.
73- Step by step :
   - once again update all step  : 
   - update config.yaml
   - update schema.yaml
   - update params.yaml
   - update the entity
   - update the configuration manager in src config
   - update the components
   - update the pipeline
   - update the main.py
   - update the app.py

   - Note in 05_model_evaluation.ipynb : 
     - joblib is a Python library that provides tools for saving and loading Python objects efficiently.
     - urllib.parse is a Python module that provides functions for parsing URLs (Uniform Resource Locators).    

74- inside " 05_model_trainer.ipynb " initials entity    
75- inside " 05_model_trainer.ipynb " update the configuration manager class and "class ConfigurationManager" .
76- inside " 05_model_trainer.ipynb " Import libraries .
77- inside " 05_model_trainer.ipynb " update the components.
78- inside " 05_model_trainer.ipynb " Update the pipeline.
79- execute code. (inside a artifacts/model_trainer/model.joblib created ).

80- update entity with src/MachineLearning_2023/entity/config_entity.
81- update configuration manager with src/MachineLearning_2023/config/configuration.py
82- update components with create a "model_trainer.py" src/MachineLearning_2023/components/model_trainer.py. 
83- update the pipeline with create a "stage_05_model_evaluation.py".
84- Add code in "main.py" for "Model Trainer stage" and then test it and before that delete a artifacts folder.
85-Run a code in GitBash-----> python main.py------> see artifacts folder. 