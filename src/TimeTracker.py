# Time Tracker

import datetime
import math
import re  # regex
import pyperclip

# import urllib3
# from bs4 import BeautifulSoup

#import RecipeItem

# Will eventually work on the scraping version


def scrape_stuff():
    pass
    # page_link = 'https://www.gameskinny.com/96m7g/kingdom-hearts-birth-by-sleep-aquas-ultimate-command-deck-guide'
    # page = urllib3.urlopen(page_link)

    # soup = BeautifulSoup(page, 'html.parser') # creates the soup object to work with -- Has one child but many descendants


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
    clip = pyperclip.paste()

    time_values = {'hours', 'minutes', 'seconds'}
    result_set = time_values.intersection(set(clip.split()))

    # true if hours, minutes, and seconds are present
    proper_format = (time_values == result_set)

    if proper_format:
        time = reg.findall(clip) # Contains (hh:mm:ss) in a list

        print("Time List: {}\n".format(time))

        hours = int(time[0])
        minutes = float( int(time[1]) / 60) # convert from minutes to decimal
        hours_worked = hours + minutes

    else:
        hours_worked = abs( float(input("Enter Your Current Hours Worked\n")) )

    return hours_worked


### Main Program ###
now = datetime.datetime.now()

# %A dictates to use the actual day of the week (Sunday - Saturday)
day = now.strftime("%A").lower()

# Time separated into Hour & Minutes
current_hour = now.hour
current_minute = now.minute


# Will set this up to read from file or use dialog setup, later
# That will help with using custom target_hours
target_hours_standard = {"monday": 8, "tuesday": 16, "wednesday": 24,
                         "thursday": 32, "friday": 40, "saturday": 48,
                         "sunday": 56}

### INPUT ###
# Whether or not you've taken your lunch. If you have, it's 0 (no time added to total) else 1
lunch_taken = ( 0 if ( input("Have you taken your lunch yet? (y/n)\n").lower() == 'y') else 1)


### VARIABLE OVERRIDE ###
# Override day / target_hours_standard values here

#day = 'monday'
### VARIABLE OVERRIDE ###

hours_worked = get_hours_worked()

# Time Remaining - Minutes & Seconds
time_remaining = target_hours_standard[day] - hours_worked

# Hours Remaining
hours_remaining = int(time_remaining)

print("Hours Remaining: " + str(hours_remaining))

# Minutes Remaining
<<<<<<< HEAD
minutes_remaining = math.ceil((float(time_remaining % 1) * 60))
=======
minutes_remaining = math.ceil( ( float(time_remaining % 1) * 60) )

print("Minutes Remaining: " + str(minutes_remaining))
>>>>>>> 5ca63e435b2d37353fa2031e10b800a3845ce18b

# Target time that the user should leave work for the day
target_hour = (current_hour + hours_remaining) + lunch_taken
target_minute = current_minute + minutes_remaining

print("Target Hour: {}\n".format(target_hour))
print("Target Minute: {}\n".format(target_minute))

target_time = to_time(target_hour, target_minute)

<<<<<<< HEAD

print("Leave work by: " + target_time)

# Some ways I run this require this to prevent automatically ending the run
=======
print("Leave work by: " + target_time)

>>>>>>> 5ca63e435b2d37353fa2031e10b800a3845ce18b
input("Press ENTER to exit")
