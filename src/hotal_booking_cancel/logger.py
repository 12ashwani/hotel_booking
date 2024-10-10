import logging
import os
from datetime import datetime

# Create logs directory if it doesn't exist
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Create log file with current timestamp
LOG_FILE = os.path.join(LOG_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

# Set up basic configuration for logging
logging.basicConfig(
    level=logging.INFO,  # Log level: INFO and above messages will be captured
    format='%(asctime)s - %(levelname)s - %(message)s',  # Log format with timestamp, level, and message
    handlers=[
        logging.FileHandler(LOG_FILE),  # Log messages to a file
        logging.StreamHandler()         # Also log messages to the console (stdout)
    ]
)

# Get the logger instance to start logging
logger = logging.getLogger()

# Example usage of logging
if __name__ == "__main__":
    logger.info("Logging setup complete.")  # Logs informational message
    logger.warning("This is a warning!")    # Logs a warning message
    logger.error("This is an error message.")  # Logs an error message



'''
logger.py is typically a module used to set up logging in a project. Logging is essential for tracking events that happen when the software runs. 
A logger.py file is used to configure the logging behavior, such as where the logs are stored (e.g., files or console), the format of the logs, and the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).

      Why Use Logging?
1 Debugging: It helps track down issues in the code.
2 Monitoring: Keeps a record of activities and errors for future reference.
3 Auditing: Logs can be useful to track how and when certain events occurred in the system. 
******
Key Components of logger.py:
Logging Levels:

DEBUG: Detailed information, typically of interest only when diagnosing problems.
INFO: Confirmation that things are working as expected.
WARNING: An indication that something unexpected happened, but the program is still running as expected.
ERROR: A more serious problem, the program may not be able to execute some functionality.
CRITICAL: A very serious error, indicating that the program itself may not be able to continue running.
Log Directory and File: The log messages are saved to a file in a logs/ directory, and a new log file is created daily using the current date in the filename.

Handlers:

FileHandler: Sends log output to a file.
StreamHandler: Sends log output to the console (stdout).
Log Format: The format specified includes:

%(asctime)s: The time when the log message was generated.
%(levelname)s: The severity level of the log.
%(message)s: The actual log message.
'''