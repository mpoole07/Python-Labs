#!/usr/bin/env python3
#
# Matthew Poole, April 7, 2026, CPT127-424, Lab11-2
#
# Program: Timer Program
# Purpose: Allow the user to start and end a timer by pressing enter and calculate how much time elapsed. 
#
# Associated file(s): none

# Insert in the output student's name and exact date/time lab was run.
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")
print()

from datetime import datetime, time

def main():
    print("The Timer program")
    print()

    # start timer
    input("Press Enter to start...")
    start_time = datetime.now()
    print(f"Start time: {start_time:%X.%f}") # format so that only the time is displayed
    print()
    
    # stop timer
    input("Press Enter to stop...")    
    stop_time = datetime.now()
    print(f"Stop time: {stop_time:%X.%f}") # format so that only the time is displayed
    print()

    # calculate elapsed time
    elapsed_time = stop_time - start_time
    days = elapsed_time.days
    minutes = elapsed_time.seconds // 60
    seconds = elapsed_time.seconds % 60
    microseconds = elapsed_time.microseconds

    # calculate hours and minutes
    hours = minutes // 60
    minutes = minutes % 60

    # create time object
    time_object = time(hours, minutes, seconds, microseconds)

    print("ELAPSED TIME")
    # display the elapsed time 
    if hours == 0 and minutes == 0:
        print(f"Seconds: {time_object:%S.%f}") # if no hours or minutes have elapsed, only display seconds
    elif days > 0:
        print("Days:", days)
        print(f"Hours/minutes: {time_object:%H:%M}")
        print(f"Seconds: {time_object:%S.%f}")
    else:
        print(f"Hours/minutes: {time_object:%H:%M}")
        print(f"Seconds: {time_object:%S.%f}")

if __name__ == "__main__":
    main()
