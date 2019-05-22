# Time Tracker

import datetime
import math
import re  # regex
import pyperclip
import os

# import urllib3
# from bs4 import BeautifulSoup

#import RecipeItem

# Will eventually work on the scraping version


def scrape_stuff():
    pass
    # page_link = 'https://www.gameskinny.com/96m7g/kingdom-hearts-birth-by-sleep-aquas-ultimate-command-deck-guide'
    # page = urllib3.urlopen(page_link)

    # soup = BeautifulSoup(page, 'html.parser') # creates the soup object to work with -- Has one child but many descendants

def create_leave_file(filename):
    
    dir_name = "C:\\Users\\kwegrowski\\Documents\\Projects"
    files = os.listdir(dir_name)

    timefile = dir_name + filename + ".leave"

    for item in files:

        if item.endswith(".leave"):
            os.remove(os.path.join(dir_name, item))

    open(timefile, 'a').close()
    print("Leave File Created")


# Converts passed in hours & minutes into Time - hh:mm[am/pm]
def to_time(hours, minutes):

    hour = 0
    minute = 0
    extra_hour = 0  # Extra hour for if/when minutes go over 60 in this calc

    if minutes > 59:
        minute = minutes - 60
        extra_hour = 1

    else:
        minute = minutes

    # Handle hours going over 24
    # This scenario is unlikely, but it's worth noting
    # that I'm handling it wrong - need to check hour + hours, not just hours
    if hours >= 24:
        hour = extra_hour + (hours - 24)

    else:
        hour += (hours + extra_hour)

    # Determine AM/PM
    day_part = ""
    if hour > 12:
        hour -= 12
        day_part = "pm"
    else:
        day_part = "am"

    # Add padding for single-digit times when necessary
    pad = ('0' if (minute < 10) else '')

    return str(hour) + ':' + (pad + str(minute)) + day_part

def get_hours_worked():

    hours_worked = None
    
    # Regex to extract hour/minute/second values
    reg = re.compile(r"\d+")

    # Get user's clipboard data
    clip = pyperclip.paste()

    time_values = {'hours', 'minutes', 'seconds'}
    
    # Will return the above values that also exist in the user's clip-data
    result_set = time_values.intersection(set(clip.split()))

    # true if hours, minutes, and seconds are present
    proper_format = (time_values == result_set)

    if proper_format:
        time = reg.findall(clip) # Contains (hh:mm:ss) in a list

        hours = int(time[0])
        minutes = float( int(time[1]) / 60) # convert from minutes to decimal
        hours_worked = hours + minutes

    else:
        hours_worked = abs( float(input("Enter Your Current Hours Worked\n")) )

    return hours_worked

def get_hours_worked_PS():

    hours_worked = None

    reg = re.compile(r"\d+")
    
    clip = pyperclip.paste()
    time = reg.findall(clip)

    hours = int(time[0])
    minutes = float( int(time[1]) / 60) # convert from minutes to decimal
    hours_worked = hours + minutes

    return hours_worked
