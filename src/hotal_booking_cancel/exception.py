import sys
import logging

# Set up logger for exception handling
logger = logging.getLogger(__name__)

class CustomException(Exception):
    """
    A custom exception class for handling application-specific errors.
    This class is designed to provide detailed error information, including the file
    and line number where the error occurred.
    """
    
    def __init__(self, error_message, error_details: sys):
        """
        Initialize the CustomException class with an error message and error details.
        
        Args:
            error_message (str): The error message describing what went wrong.
            error_details (sys): The system information to extract details about the exception.
        """
        super().__init__(error_message)
        self.error_message = CustomException.get_detailed_error_message(error_message, error_details)  # Generate detailed error message
    
    @staticmethod
    def get_detailed_error_message(error_message, error_details: sys):
        """
        Format and return a detailed error message with information about the file
        and line number where the exception occurred.
        
        Args:
            error_message (str): The initial error message.
            error_details (sys): The system information containing exception details.
        
        Returns:
            str: A detailed error message with file name and line number.
        """
        _, _, exc_tb = error_details.exc_info()  # Extract traceback from error details
        file_name = exc_tb.tb_frame.f_code.co_filename  # Get the file name where the exception occurred
        line_number = exc_tb.tb_lineno  # Get the line number where the exception occurred
        error_message = f"Error occurred in script: {file_name} at line {line_number}: {error_message}"  # Construct detailed error message
        return error_message
    
    def __str__(self):
        """
        Return the detailed error message when the exception is printed or logged.
        
        Returns:
            str: The detailed error message.
        """
        return self.error_message


# Example of another custom exception extending the base CustomException class
class DataIngestionException(CustomException):
    """
    Exception raised for errors in the data ingestion process.
    This inherits from the CustomException class, allowing it to provide detailed error information
    specific to data ingestion failures.
    """
    pass


# Example usage to demonstrate how the CustomException works
if __name__ == "__main__":
    try:
        # Simulate an error (division by zero in this case)
        x = 1 / 0
    except Exception as e:
        # Raise a custom exception with the original error message and system details
        raise CustomException("Division by zero error", sys)
