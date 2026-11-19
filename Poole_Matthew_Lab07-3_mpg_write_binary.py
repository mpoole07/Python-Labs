#!/usr/bin/env python3
#
# Matthew Poole, March 1, 2026, CPT-127-424, Lab07-3
#
# Program: Miles Per Gallon Program
# Purpose: Calculate the Miles Per Gallon and store the trips in a bin file
#
# Associated file(s): trips.bin

# Insert in the output student's name and exact date/time lab was run.
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")

import pickle # import pickle so bin files can be used

TRIPSFILE = "trips.bin" # make constant TRIPSFILE represent trips.bin

# get input from the user of miles driven and test to make sure it is valid
def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven

# get input from the user of the gallons used and test to make sure it is valid
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

# writes the stored data in trips into the trips.bin file
def write_trips(trips):
    with open(TRIPSFILE, mode="wb") as file:
        pickle.dump(trips, file)
        
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    trips = [] # initialize a list to store trips

    more = "y"
    # ask the user to input the values, then calculate mpg and repeat if needed.
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        trips.append([miles_driven, gallons_used, mpg]) # adds data to the trips 2d list

        # ask the user if they want to enter another trip
        more = input("More entries? (y or n): ")
        
    # saves the trip data to the file
    write_trips(trips)
    
    print("Bye!")

if __name__ == "__main__":
    main()

