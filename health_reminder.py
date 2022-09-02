# Import required Libraries
import os
import sys
import random
from time import time
from pygame import mixer
from datetime import datetime
from plyer import notification
from health_reminder.exception import ReminderCustomException
from health_reminder.utils.get_facts import *
from health_reminder.config.configuration import ReminderConfiguration
from health_reminder.logging import logger
from health_reminder.constants import *


# Getting information from entity
appconfig = ReminderConfiguration()
user_info = appconfig.get_interval_config()
app_info = appconfig.get_app_config()
audio_dir = app_info.audio_dir
icon_dir = app_info.icon_dir
timelog_dir = app_info.timelog_dir


# Creating the reminder App fucntions 
def music_function(music_file):
    '''
    Fucntion to play music with music_file
    '''
    try:
        mixer.init()
        mixer.music.load(music_file)
        mixer.music.play()
        while True:
            logger.info(f"Music playing: at {CURRENT_TIME_STAMP}") 
            command = user_info.user_commands
            userinput = input(
                f"""Please type any one of the following {command} to stop reminder music:""")
            if userinput in command:
                mixer.music.stop()
                break
    except Exception as e:
        message = ReminderCustomException(e, sys)
        logger.error("Error in Music function: ", message.error_message)


def Drinkwater():
    '''
    Function for Drink water reminder
    '''
    try:
        water_facts = get_water_facts()
        logger.info("Reminder to Drink water!")
        print("Drink water now !!!")
        notification.notify(
            title="Drink water",
            message=random.choice(water_facts),
            app_icon=os.path.join(icon_dir, WATERICO),
            timeout=13
        )
        music_function(os.path.join(audio_dir, WATERMP3))

        with open(os.path.join(timelog_dir, REMINDLOGS), 'a+') as f:
            f.write(f'Water Drank at: {str(datetime.now())}\n')
        print("Your Response has been stored in reminder_timelog directory")
    except Exception as e:
        message = ReminderCustomException(e, sys)
        logger.error("Error in Drinkwater function: ", message.error_message)


def Workout():
    '''
    Function for Workout reminder
    '''
    try:
        exercise_facts = get_exercise_facts()
        logger.info("Workout reminder !")
        print("Start yout workout now !!!")
        notification.notify(
            title="Time for workout break",
            message=random.choice(exercise_facts),
            app_icon=os.path.join(icon_dir, WORKOUTICO),
            timeout=13
        )
        music_function(os.path.join(audio_dir, WORKOUTMP3))

        with open(os.path.join(timelog_dir, REMINDLOGS), 'a+') as f:
            f.write(f'Workout done at: {str(datetime.now())}\n')
        print("Your Response has been stored in reminder_timelog directory")
    except Exception as e:
        message = ReminderCustomException(e, sys)
        logger.error("Error in Workout function: ", message.error_message)


def Eye():
    '''
    Fucntion for Eye relax reminder
    '''
    try:
        eye_facts = get_eye_facts()
        print("Relax your eyes")
        notification.notify(
            title="Relax your eyes now",
            message=random.choice(eye_facts),
            app_icon=os.path.join(icon_dir, EYESICO),
            timeout=13
        )
        music_function(os.path.join(audio_dir, EYESMP3))
        with open(os.path.join(timelog_dir, REMINDLOGS), 'a+') as f:
            f.write(f'Eyes relaxed at: {str(datetime.now())}\n')
        print("Your Response has been stored in reminder_timelog directory")
    except Exception as e:
        message = ReminderCustomException(e, sys)
        logger.error("Error in Eye function: ", message.error_message)


if __name__ == '__main__':
    
    logger.info(f"App has been started at {CURRENT_TIME_STAMP}")

    # Get seconds from time method
    waterTime = time()
    workoutTime = time()
    eyeTime = time()

    # Setting the reminder times can be reduced in config.yaml file while testing
    water_reminder = user_info.drinkwater_interval*60  # 15 minutes
    workout_reminder = user_info.workout_interval*60  # 1hr 30 minutes
    eyes_reminder = user_info.eyes_relax_interval*60  # 30 minutes

    # Running the reminder function
    while True:
        current_time = time()
        if current_time - waterTime > water_reminder:
            Drinkwater()
            waterTime = time()
        if current_time - workoutTime > workout_reminder:
            Workout()
            workoutTime = time()
        if current_time - eyeTime > eyes_reminder:
            Eye()
            eyeTime = time()
