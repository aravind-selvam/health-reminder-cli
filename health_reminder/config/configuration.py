import os 
import sys 
from health_reminder.exception import ReminderCustomException
from health_reminder.logging import logger
from health_reminder.utils import read_yaml_file
from health_reminder.entity.app_entity import Application_config, Interval_config
from health_reminder.constants import *

class ReminderConfiguration:
    """
    Class Reminderconfig which provides configuration to config.yaml file and entity
    """
    def __init__(self, config_file_path: str = CONFIG_FILE_PATH,
                 current_time:str = CURRENT_TIME_STAMP
                 )-> None:
        """
        Initialize ReminderConfig

        Args:
            config_file_path (str): Defaults to CONFIG_FILE_PATH.
            current_time (str): Defaults to CURRENT_TIME_STAMP.

        Raises:
            ReminderCustomException: Error raised with exact line numbers and module name
        """
        try:
            self.yaml_info = read_yaml_file(file_path= config_file_path)
        except Exception as e:
            raise ReminderCustomException(e, sys)from e 
    
    def get_app_config(self)-> Application_config:
        """
        Gets the configuration from yaml file

        Raises:
            ReminderCustomException: Error raised with exact line numbers and module name

        Returns:
            Application_config: App config which gets information from config.yaml 
                and stores to Application_config entity
        """
        try:
            app_config = self.yaml_info[APP_KEY]
            app_name = app_config[APPLICATION_NAME]
            resources_key = app_config[RESOURCES_KEY]
            resources_dir= os.path.join(ROOT_DIR,
                                        app_name,
                                        resources_key
                                        )
            os.makedirs(resources_dir, exist_ok=True)
            
            audio_dir = os.path.join(resources_dir,
                                     app_config[AUDIO_KEY])
            os.makedirs(audio_dir, exist_ok=True)
            
            icon_dir = os.path.join(resources_dir, 
                                    app_config[ICON_KEY])
            os.makedirs(icon_dir, exist_ok=True)
            
            logs_dir = os.path.join(ROOT_DIR,
                                    app_config[LOGSKEY])
            os.makedirs(logs_dir, exist_ok=True)
            
            timelog_dir = os.path.join(logs_dir,
                                       app_config[TIMELOGS_KEY])
            os.makedirs(timelog_dir, exist_ok=True)
            
            app_config = Application_config(app_name=app_name,
                                            resources_dir=resources_dir,
                                            logs_dir=logs_dir,
                                            audio_dir=audio_dir,
                                            icon_dir=icon_dir,
                                            timelog_dir=timelog_dir)
            logger.info(f"App logs and resources path configured.{app_config}")
            return app_config
        except Exception as e:
            raise ReminderCustomException(e,sys)from e
    
    def get_interval_config(self)-> Interval_config:
        """
        get interval configuration from yaml file

        Raises:
            ReminderCustomException: Error raised with exact line number and module
        Returns:
            Interval_config: Interval configuration App entity
        """
        try:
            interval_config = self.yaml_info[INTERVAL_KEY]
            workout_interval = interval_config[WORKOUT_INT]
            drinkwater_interval = interval_config[DRINK_INT]
            eyes_relax_interval = interval_config[EYE_INT]
            user_commands = interval_config[USER_CMD]
            
            interval_config = Interval_config(workout_interval = workout_interval,
                                              drinkwater_interval=drinkwater_interval,
                                              eyes_relax_interval=eyes_relax_interval,
                                              user_commands=user_commands
                                              )
            logger.info(f"Interval for reminder is configured.{interval_config}")
            return interval_config
        except Exception as e:
            raise ReminderCustomException(e, sys)from e