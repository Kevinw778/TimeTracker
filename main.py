import datetime
import math
import re  # regex
import pyperclip
from enum import Enum, unique

import timetracker as tt

### Main Program ###
now = datetime.datetime.now()

# %A dictates to use the actual day of the week (Sunday - Saturday)
day = now.strftime("%A").lower()

# Time separated into Hour & Minutes
current_hour = now.hour
current_minute = now.minute


# Will set this up to read from file or use dialog setup, later
# That will help with using custom target_hours
TARGET_HOURS_STANDARD = {"monday": 8, "tuesday": 16, "wednesday": 24,
                         "thursday": 32, "friday": 40, "saturday": 48,
                         "sunday": 56}
						 
TARGET_HOURS_MODIFIED = {"monday": 8, "tuesday": 8, "wednesday": 16,
                         "thursday": 24, "friday": 32, "saturday": 48,
                         "sunday": 56}

# target_hours = TARGET_HOURS_STANDARD
target_hours = TARGET_HOURS_STANDARD

### INPUT ###
# Whether or not you've taken your lunch. If you have, it's 0 (no time added to total) else 1
lunch_taken = 0 #lunch_taken = ( 0 if ( input("Have you taken your lunch yet? (y/n)\n").lower() == 'y') else 1)


### VARIABLE OVERRIDE ###
#day = 'monday'
### VARIABLE OVERRIDE ###


hours_worked = tt.get_hours_worked_PS()

# Time Remaining - Minutes & Seconds
time_remaining = target_hours[day] - hours_worked

# Hours Remaining
hours_remaining = int(time_remaining)

# Minutes Remaining
minutes_remaining = math.ceil( ( float(time_remaining % 1) * 60) )

# Target time that the user should leave work for the day
target_hour = (current_hour + hours_remaining) + lunch_taken
target_minute = current_minute + minutes_remaining

target_time = tt.to_time(target_hour, target_minute)

print("Time Worked:", int(hours_worked//1), "hours ", int( (hours_worked%1 * 60) ), "minutes\n")

print("\nLeave work by: " + target_time + '\n')

# tt.create_leave_file(str(target_time))

input("Press ENTER to exit")


