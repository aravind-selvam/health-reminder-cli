# Health Reminder application using Python
![](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![](https://img.shields.io/badge/CLI-000000?style=for-the-badge&logo=clion&logoColor=white)

Health Reminder is a python application that uses pygame and plyer to remind the user to drink water, workout, and relax their eyes.

## How to run?
### STEPS:

Clone the repository

```
https://github.com/aravind9722/Health_reminder.py.git
```
### STEP 01- Create a conda environment after opening the repository

```
conda create -p venv python=3.9.12 -y
```

```
conda activate venv
```

### STEP 02- install the requirements
```
pip install -r requirements.txt
```
### STEP 03- Change your input you need in Config.yaml interval_config
```
interval_config:
  workout_interval: 10
  drinkwater_interval: 10
  eyes_relax_interval: 30
  user_commands:
    - DONE
    - done
    - Done
```
### STEP 03- run app
```
python health_reminder.py
```

- **Timelogs of our work are stored in all_logs directory in timelogs folder**
- **Application logs are stored in all_logs directory pylogs folder.**

## Demo
### Workout Reminder
![workout](imagemd/workout.png)
### Water Reminder
![drinkwater](imagemd/water.png)
### Eyerelax Reminder
![eye](imagemd/eyes.png)

## Built With

1. Pygame
2. Plyer 
3. Python (Python 3.9.12)

## Contributions
Please feel free to fork this repository and submit pull requests. Any contributions are welcome and appreciated!

## Contact
For any questions or feedback, please contact me at: aravind_selvam@outlook.com

## License
This project is licensed under the [MIT License](https://github.com/aravind-selvam/Text-to-Speech-web-application/blob/main/LICENSE)

## Acknowledgments
Python
Pygame
Plyer
