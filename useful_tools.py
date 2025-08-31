import random

feet_in_mile = 5280
meters_in_kilometers = 1000
beatles = ["Sachin Sen", "Rahul Sen", "Krishna Sen"]

def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

def roll_dice(num):
    return random.radint(1, num)