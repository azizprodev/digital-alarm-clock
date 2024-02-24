# alarm clock
# playsound(to play music file) and time(use for time) module
from playsound import playsound
import time

# Escape sequence: ANSI escape codes
CLEAR = '\033[2J'  # This sequence clears the entire screen or terminal window.
CLEAR_AND_RETURN = '\033[H' # This sequence moves the cursor to the home position, typically the upper-left corner of the screen.

# function to set time and play sound
def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
    
    playsound("alarm.mp3")


# input from user to set minutes and seconds
minutes = int(input("Enter minutes to wait: "))
seconds = int(input("Enter seconds to wait: "))

# convert minutes to seconds
total_seconds = minutes * 60 + seconds

# call the function
alarm(total_seconds)