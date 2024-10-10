import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the project name
project_name = 'hotal_booking_cancel'

# List of files and directories to create
list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",  # Corrected "model_tranier.py" to "model_trainer.py"
    f"src/{project_name}/components/model_monitoring.py",  # Corrected "model_monitering.py" to "model_monitoring.py"
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

# Create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)  # Create a Path object
    filedir, filename = os.path.split(filepath)  # Split the path into directory and filename

    # Create directories if they do not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # Create an empty file if it does not exist or if it is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # Create an empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")

logging.info("Project structure created successfully.")
