# Import required libraries
import logging
import os
from datetime import datetime 

# Creating logs directory to store log in files
LOG_DIR = "all_logs/pylogs"
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

# Creating directory if it does not exists.
os.makedirs(LOG_DIR, exist_ok=True)

fmt = "%Y-%m-%d %H%M%S"
CURRENT_TIME_STAMP = datetime.now().strftime(fmt)
#Creating file with name as file_name.
file_name = f"log_{CURRENT_TIME_STAMP}.log"
log_file_path = os.path.join(LOG_DIR, file_name)

# Create and configure logging
logging.basicConfig(level= logging.DEBUG,
                    filename=log_file_path,
                    format='%(asctime)s %(levelname)s %(module)s ====> %(message)s',
                    datefmt= "%d-%m-%Y %H:%M")

#Create object for logging with level info 
logger = logging.getLogger()