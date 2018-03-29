# Time Tracker

import datetime
import math
import re #regex
import pyperclip

import urllib3
from bs4 import BeautifulSoup

#import RecipeItem

# Will eventually work on the scraping version
def scrapeStuff():

    pageLink = 'https://www.gameskinny.com/96m7g/kingdom-hearts-birth-by-sleep-aquas-ultimate-command-deck-guide'
    page = urllib3.urlopen(pageLink)

    soup = BeautifulSoup(page, 'html.parser') # creates the soup object to work with -- Has one child but many descendants


# Converts passed in hours & minutes into Time - hh:mm[am/pm]
def toTime(hours, minutes):

    hour = 0
    minute = 0
    extraHour = 0 # Extra hour for if/when minutes go over 60 in this calc

    if (minutes > 59):
        minute = (minutes - 60)
        extraHour = 1

    else:
        minute = minutes

    # Honestly most of this is overkill -- input won't generally cross these cases
    if (hours >= 24):
        hour = 1 + extraHour + (hours - 24)

    else:
        hour += (hours + extraHour)

    # Determine AM/PM
    dayPart = ""
    if (hour > 12):
        hour -= 12
        dayPart = "pm"
    else:
        dayPart = "am"

    # Add padding for single-digit times when necessary
    pad = ('0' if (minute < 10) else '')

    return ( str(hour) + ':' + ( pad + str(minute) ) + dayPart )


### Main Program ###
now = datetime.datetime.now()

# %A dictates to use the actual day of the week (Sunday - Saturday)
day = now.strftime("%A").lower()

# Time separated into Hour & Minutes
timeHour = now.hour
timeMinute = now.minute


# Will set this up to read from file, later
# That will help with using custom targetHours
targetHoursStandard = {"monday": 8, "tuesday": 16, "wednesday": 24,
                       "thursday": 32, "friday": 40, "saturday": 48,
                       "sunday": 56}

# Keeping this for when I implement the "either or" option of data-entry
# INPUT #
# Number of hours worked this week
#hoursWorked = abs( float(input("Enter Your Current Hours Worked\n")) )

### INPUT ###
# Whether or not you've taken your lunch. If you have, it's 0 (no time subtracted from total) else 1
lunchTaken = ( 0 if ( input("Have you taken your lunch yet? (y/n)\n").lower() == 'y') else 1)


### VARIABLE OVERRIDE ###
#day = 'monday'
### VARIABLE OVERRIDE ###

# Regular expression to parse the time info in clipboard
reg = re.compile(r"\d+")

clip = pyperclip.paste()

time = reg.findall(clip) # Contains (hh:mm:ss) in a list

# Break the time up into pieces and convert into #'s instead of strings
hours = int(time[0])
minutes = float( int(time[1]) / 60 ) # convert from minutes to decimal

hoursWorked = hours + minutes

# Time Remaining - Minutes & Seconds
timeRemaining = targetHoursStandard[day] - hoursWorked

# Hours Remaining
#hoursRemaining = int(time[0])
hoursRemaining = int(timeRemaining)

# Minutes Remaining
#minutesRemaining = int(time[1])
minutesRemaining = math.ceil( ( float(timeRemaining % 1) * 60) )

# Target time that the user should leave work for the day
targetHour = (timeHour + hoursRemaining) + lunchTaken
targetMinute = timeMinute + minutesRemaining

targetTime = toTime(targetHour, targetMinute)

# This is calculating 5-hours off for some reason... Look into this -
# simulate the day when I get home
print("Leave work by: " + targetTime)

#for n in time:
#    print (n)

input("Press ENTER to exit")
