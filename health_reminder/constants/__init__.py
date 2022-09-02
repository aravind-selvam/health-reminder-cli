import os 
from datetime import datetime
from health_reminder.utils import read_yaml_file
# from health_reminder.config.configuration import ReminderConfiguration


def get_current_time():
    """
    Gets the current time with custom time format
    """
    fmt = "%Y-%m-%d %H%M%S"
    return f"{datetime.now().strftime(fmt)}"

ROOT_DIR = os.getcwd()
CONFIG_FOLDERNAME = "config"
CONFIG_FILENAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_FOLDERNAME, CONFIG_FILENAME)

CURRENT_TIME_STAMP = get_current_time()

# appinfo = ReminderConfiguration().get_app_config()
# applogdir = appinfo.applog_dir
# APPLOGDIR = applogdir

yaml_info = read_yaml_file(file_path = CONFIG_FILE_PATH)
filenames = yaml_info["file_names"]
# file_names constants are defined
WATERICO = filenames["waterico"]
WATERMP3 = filenames["watermp3"]
WORKOUTICO = filenames["workoutico"]
WORKOUTMP3 = filenames["workoutmp3"]
EYESICO = filenames["eyesico"]
EYESMP3 = filenames["eyesmp3"]
REMINDLOGS = filenames["timelogs"]

# Application configuration
APP_KEY = "application_config"
APPLICATION_NAME = "app_name"
LOGSKEY = "logs_dir"
RESOURCES_KEY = "resources_dir"
ICON_KEY = "icon_dir"
AUDIO_KEY = "audio_dir"
TIMELOGS_KEY = "timelog_dir"
APPLOG_KEY = "applog_dir"

# Changing interval settings
INTERVAL_KEY = "interval_config"
WORKOUT_INT = "workout_interval"
DRINK_INT = "drinkwater_interval"
EYE_INT = "eyes_relax_interval"
USER_CMD = "user_commands"