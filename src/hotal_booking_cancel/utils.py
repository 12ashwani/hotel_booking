'''
The utils.py file in a project typically contains utility functions that are shared across different parts of the codebase. These functions generally perform common, repetitive tasks that don't belong to a specific module or component. The goal of a utils.py file is to help organize the project by providing reusable code in one place, making the codebase cleaner and more maintainable.

Why Use a utils.py?
Reusability: Functions that are used across multiple modules can be centralized.
Separation of Concerns: It keeps the main logic (e.g., data processing, model training) separate from helper functions.
Maintainability: Easier to maintain as utility functions are located in one file.
Common Types of Functions in utils.py:
File operations (reading/writing files)
Data processing helper functions
Logging utilities
Performance monitoring functions
Math/statistical calculations
Helper functions for handling configuration
Example utils.py File:'''

import os
import pandas as pd
import json
import pymysql
import requests  # Import requests to handle API calls
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from src.hotal_booking_cancel.logger import logging
from src.hotal_booking_cancel.exception import CustomException
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
load_dotenv()  # Load environment variables from a .env file

# Environment variables for database connection
host = os.getenv('host')
user = os.getenv('user')
pas = os.getenv('password')
db = os.getenv('db')

def read_sql_data():
    logging.info('Reading the SQL data...')
    try:
        # Establishing a connection to the SQL database
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=pas,
            db=db
        )
        logging.info('Connection successful: %s', mydb)

        # Reading the data from a specific table
        df = pd.read_sql_query('SELECT * FROM hotel', mydb)
        mydb.close()  # Closing the connection to the database
        return df
    except Exception as ex:
        logging.error(f"Error occurred while reading SQL data: {ex}")
        raise CustomException(f"Error occurred while reading SQL data: {ex}")

# 1. Function to read a CSV file
def read_csv_file(file_path):
    """
    Reads a CSV file into a pandas DataFrame.
    :param file_path: Path to the CSV file
    :return: pandas DataFrame
    """
    try:
        df = pd.read_csv(file_path)
        logger.info(f"CSV file at {file_path} successfully loaded.")
        return df
    except FileNotFoundError:
        logger.error(f"CSV file at {file_path} not found.")
        raise
    except Exception as e:
        logger.error(f"Error occurred while reading CSV file at {file_path}: {e}")
        raise

# 2. Function to save a DataFrame to a CSV file
def save_csv_file(df, file_path):
    """
    Saves a pandas DataFrame to a CSV file.
    :param df: DataFrame to save
    :param file_path: Path to save the CSV file
    """
    try:
        df.to_csv(file_path, index=False)
        logger.info(f"Data successfully saved to {file_path}")
    except Exception as e:
        logger.error(f"Error occurred while saving data to {file_path}: {e}")
        raise

# 3. Function to read data from an API
def read_api_data(api_url):
    """
    Reads data from an API and converts it into a pandas DataFrame.
    :param api_url: URL of the API to read data from
    :return: pandas DataFrame containing the API data
    """
    logger.info(f'Reading data from API: {api_url}')
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
        
        data = response.json()  # Parse the response as JSON
        df = pd.DataFrame(data)  # Convert the JSON data into a pandas DataFrame
        logger.info(f"Data successfully loaded from API: {api_url}")
        return df
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        raise CustomException(f"HTTP error occurred: {http_err}")
    except Exception as e:
        logger.error(f"Error occurred while reading data from API: {e}")
        raise CustomException(f"Error occurred while reading data from API: {e}")


# 3. Function to evaluate classification model performance
def evaluate_model_performance(y_true, y_pred):
    """
    Evaluates a classification model using common metrics: accuracy, precision, recall, and F1-score.
    :param y_true: Actual target labels
    :param y_pred: Predicted target labels
    :return: Dictionary of evaluation metrics
    """
    try:
        metrics = {
            'accuracy': accuracy_score(y_true, y_pred),
            'precision': precision_score(y_true, y_pred, average='weighted'),
            'recall': recall_score(y_true, y_pred, average='weighted'),
            'f1_score': f1_score(y_true, y_pred, average='weighted')
        }
        logger.info(f"Model performance evaluated: {metrics}")
        return metrics
    except Exception as e:
        logger.error(f"Error occurred during model evaluation: {e}")
        raise

# 4. Function to load a JSON configuration file
def load_json_config(config_path):
    """
    Loads a JSON configuration file.
    :param config_path: Path to the configuration file
    :return: Dictionary containing configuration parameters
    """
    try:
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
        logger.info(f"Configuration loaded from {config_path}")
        return config
    except FileNotFoundError:
        logger.error(f"Configuration file not found at {config_path}")
        raise
    except json.JSONDecodeError:
        logger.error(f"Error decoding JSON file at {config_path}")
        raise
    except Exception as e:
        logger.error(f"Error loading JSON configuration: {e}")
        raise

# 5. Function to check if a directory exists, if not, create it
def ensure_directory_exists(dir_path):
    """
    Ensures that a directory exists; if not, it creates the directory.
    :param dir_path: Path to the directory
    """
    try:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            logger.info(f"Directory {dir_path} created.")
        else:
            logger.info(f"Directory {dir_path} already exists.")
    except Exception as e:
        logger.error(f"Error creating directory {dir_path}: {e}")
        raise
