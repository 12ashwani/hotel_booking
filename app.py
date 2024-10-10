from src.hotal_booking_cancel.exception import CustomException
from src.hotal_booking_cancel.logger import logging
from src.hotal_booking_cancel.components.data_ingestion import DataIngestion
from src.hotal_booking_cancel.components.data_ingestion import DataIngestionConfig

import sys

if __name__ == '__main__':
   if __name__ == "__main__":
    logging.info("Logging setup complete.")
    # logger.warning("This is a warning!")
    # logger.error("This is an error message.")
    try:
        # Simulate an error
        # data_ingetion_confi=DataIngestionConfig()
        data_inge=DataIngestion()
        data_inge.ingest_database()
    except Exception as e:
        # logging.info("custome  setup complete.")

        raise CustomException("Division by zero error", sys)
