import os
import sys
import random
from time import time
from pygame import mixer
from datetime import datetime
from plyer import notification
from reminder_logging import logger
from reminder_utils.get_facts import *
from reminder_exception import ReminderCustomException

# get path to resources
resources_path = os.path.join(os.path.dirname(__file__), 'reminder_resources')
os.makedirs("reminder_timelogs", exist_ok=True)

def music_function(music_file):
    '''
    Fucntion to play music with music_file
    '''
    try:
        mixer.init()
        mixer.music.load(music_file)
        mixer.music.play()
        while True:
            userinput = input("Please type DONE to stop reminder music:")
            command = ["DONE", "done", "Done"]
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
        print("Drink water now !!!")
        notification.notify(
            title = "Drink water",
            message = random.choice(water_facts),
            app_icon=os.path.join(resources_path,"icons/waters.ico"),
            timeout = 13
        )
        music_function(os.path.join(resources_path, "audio\waters.mp3"))
        with open(os.path.join("reminder_timelogs/waterlog.txt"), 'a+') as f:
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
        print("Start yout workout now !!!")
        notification.notify(
            title = "Time for workout break",
            message = random.choice(exercise_facts),
            app_icon = os.path.join(resources_path,"icons/workout.ico"),
            timeout = 13
        )
        music_function(os.path.join(resources_path,"audio/workout.mp3"))
        with open("reminder_timelogs/workout.txt", 'a+') as f:
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
            title = "Relax your eyes now",
            message =  random.choice(eye_facts),
            app_icon = os.path.join(resources_path, "icons/eyes.ico"),
            timeout = 13
        )
        music_function(os.path.join(resources_path, "audio/eyes.mp3"))
        with open("reminder_timelogs/eye.txt", 'a+') as f:
            f.write(f'Eyes relaxed at: {str(datetime.now())}\n')
        print("Your Response has been stored in reminder_timelog directory")
    except Exception as e:
        message = ReminderCustomException(e, sys)
        logger.error("Error in Eye function: ", message.error_message)

if  __name__ == '__main__':
    
    # Get seconds from time method
    waterTime = time()
    workoutTime = time()
    eyeTime = time()
    
    #Setting the reminder times can be reduced while testing
    water_reminder  = 15*60 # 15 minutes
    workout_reminder = 90*60 # 1hr 30 minutes
    eyes_reminder = 40*60 # 40 minutes
    
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
        