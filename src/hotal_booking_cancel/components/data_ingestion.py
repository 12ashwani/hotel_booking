import pandas as pd
import requests
import logging
import os
from dataclasses import dataclass
from src.hotal_booking_cancel.utils import read_sql_data
from sklearn.model_selection import train_test_split

# Set logging configuration for tracking the program's execution
logging.basicConfig(level=logging.INFO)

# DataIngestionConfig class holds the file paths for storing raw, train, and test datasets
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("Data_folder", 'train.csv')
    test_data_path: str = os.path.join("Data_folder", 'test.csv')
    raw_data_path: str = os.path.join("Data_folder", 'raw_data.csv')  # Corrected variable name

# DataIngestion class handles various ways of ingesting data (CSV, database, API)
class DataIngestion:
    def __init__(self):
        """Initialize the DataIngestion class with default configuration paths."""
        self.ingestion_config = DataIngestionConfig()  # Initialize the ingestion config

    def ingest_csv(self, file_path):
        """
        This function ingests data from a CSV file and returns it as a pandas DataFrame.
        
        Args:
            file_path (str): Path to the CSV file.

        Returns:
            DataFrame: Ingested CSV data as a pandas DataFrame or None if an error occurs.
        """
        try:
            df = pd.read_csv(file_path)
            logging.info("CSV data ingested successfully.")
            return df
        except Exception as e:
            logging.error(f"Error during CSV ingestion: {e}")
            return None

    def ingest_database(self):
        """
        This function ingests data from a database using a custom read_sql_data function,
        splits the data into training and test sets, and saves them as CSV files.

        Returns:
            tuple: A tuple containing the training and test datasets as pandas DataFrames,
                   or None if an error occurs.
        """
        try:
            # Fetch data from the database
            df = read_sql_data()
            logging.info("Database data ingested successfully.")

            # Ensure the Data_folder directory exists for saving files
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # Save the entire raw dataset to CSV
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Split the data into training and test sets (80% train, 20% test)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save the train and test sets as CSV files
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Data ingestion is complete')

            return train_set, test_set  # Return the train and test DataFrames

        except Exception as e:
            logging.error(f"Error during database ingestion: {e}")
            return None

    def ingest_api(self, api_url):
        """
        This function ingests data from an API by sending a GET request and converting
        the response into a pandas DataFrame.

        Args:
            api_url (str): URL of the API endpoint.

        Returns:
            DataFrame: Ingested API data as a pandas DataFrame or None if an error occurs.
        """
        try:
            # Send GET request to the API and handle response
            response = requests.get(api_url)
            response.raise_for_status()  # Raise an HTTPError for bad responses
            data = response.json()  # Parse the JSON response into Python dictionary

            # Convert the JSON data into a pandas DataFrame
            df = pd.DataFrame(data)
            logging.info("API data ingested successfully.")
            return df

        except Exception as e:
            logging.error(f"Error during API ingestion: {e}")
            return None
