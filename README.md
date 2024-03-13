
# Wine Quality Prediction: End-to-End Machine Learning Project

## Overview
This project is a sophisticated end-to-end machine learning pipeline designed for predicting wine quality from physicochemical attributes. Bridging the gap between traditional wine quality assessment and modern data science, this pipeline encompasses all stages from data processing to model deployment.

## Data Description
The dataset, hosted on [my GitHub profile](https://github.com/farshidhesami/machine_learning_01), features red wine samples each characterized by a range of chemical attributes. The primary goal is to predict the quality of wine, quantified on a scale from 0 to 10, using these attributes.

## Pipeline and Configuration Updates

### Pipeline Stages
1.  Data Ingestion  (`01_data_ingestion.ipynb`): Ingesting the dataset for preliminary exploration.
2.  Data Validation  (`02_data_validation.ipynb`): Verifying data quality and integrity.
3.  Data Transformation  (`03_data_transformation.ipynb`): Preprocessing data for effective model training.
4.  Model Training  (`04_model_trainer.ipynb`): Training the machine learning model.
5.  Model Evaluation   (`05_model_evaluation.ipynb`): Assessing the model's performance.
6.  Prediction  (`prediction.py`): Implementing the model for predictions.
7.  Web Application  (`app.py`): Creating a Flask web application for interactive model utilization.

### Configuration and Deployment
1.  Update config.yaml : Setting configurations for the project.
2.  Update schema.yaml : Defining data schema for accurate validation.
3.  Update params.yaml : Specifying parameters for the model training process.
4.  Update the Entity : Adjusting data model entities as required.
5.  Update the Configuration Manager in src/config : Managing configurations for the project.
6.  Update the Components : Refining modular components of the project.
7.  Update the Pipeline : Enhancing the data processing and ML pipeline.
8.  Update main.py : Finalizing the main execution script.
9.  Update app.py : Improving the Flask web application for enhanced user engagement.

## Getting Started

### Prerequisites
- Python 3.8
- Pip (Python package manager)
- Visual Studio Code or any IDE/Code Editor

### Installation and Setup
1.  Clone the Repository : 
   ```bash
   git clone https://github.com/farshidhesami/machine_learning_01.git
   ```
2.  Navigate to the Project Directory :
   ```bash
   cd machine_learning_01
   ```
3.  Install Dependencies :
   ```bash
   pip install -r requirements.txt
   ```
4.  Initialize the Project Structure :
   ```bash
   python template.py
   ```

### Usage
1.  Run the Main Pipeline :
   ```bash
   python main.py
   ```
2.  Web Application :
   ```bash
   python app.py
   ```
- Access the web application at [http://127.0.0.1:8080] for inputs and predictions, and [http://127.0.0.1:8080/predict] for the interactive prediction interface.

## Web Application Input Interface

![Web Application Input Data](https://github.com/farshidhesami/machine_learning_01/blob/main/image/web%20application%20input%20data.jpg)

## Web Application Prediction Interface

![Web Application Predict](https://github.com/farshidhesami/machine_learning_01/blob/main/image/web%20application%20predict.jpg)

## File Structure
- `src/`: Core source code.
- `data/`: Wine quality dataset.
- `artifacts/`: Generated models and reports.
- `research/`: Jupyter notebooks for analysis.
- `template.py`: Initial project setup script.
- `requirements.txt`: Project dependencies.
- `main.py`: Main script for the ML pipeline.
- `app.py`: Flask application for model deployment.

## Contact
-  Farshid Hesami :
  -  GitHub : [Farshid Hesami's GitHub](https://github.com/farshidhesami)
  -  LinkedIn : [Farshid Hesami on LinkedIn](https://linkedin.com/in/farshidhesami)

## Acknowledgments
This project is a showcase of how machine learning can bring a new level of precision and objectivity to traditional industries like wine making, demonstrating the potential for data-driven decision-making in enhancing quality assessment processes.
