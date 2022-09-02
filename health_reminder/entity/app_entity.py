from collections import namedtuple

Application_config = namedtuple("Application_config", ["app_name",
                                                       "logs_dir", 
                                                       "resources_dir",
                                                       "timelog_dir",
                                                       "audio_dir",
                                                       "icon_dir",
                                                       ])

Interval_config = namedtuple("Interval_config", ["workout_interval",
                                                "drinkwater_interval",
                                                "eyes_relax_interval",
                                                "user_commands"
                                                ])