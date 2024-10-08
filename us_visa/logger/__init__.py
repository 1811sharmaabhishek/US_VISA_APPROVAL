import logging
import os
from from_root import from_root
from datetime import datetime

# Define the log file name based on current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory structure for logs using from_root
logs_dir_path = 'D:/US_VISA_APPROVAL/logs'  # Full path for the `logs` directory
logs_path = os.path.join(logs_dir_path, LOG_FILE)  # Full path for the log file

# Create the `logs` directory if it doesn't exist
os.makedirs(logs_dir_path, exist_ok=True)

# Set up the logging configuration
logging.basicConfig(
    filename=logs_path,
    format="[%(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)