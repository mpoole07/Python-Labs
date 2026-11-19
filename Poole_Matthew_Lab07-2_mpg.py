#!/usr/bin/env python3
#
# Matthew Poole, March 1, 2026, CPT-127-424, Lab07-2
#
# Program: Miles Per Gallon Program
# Purpose: Calculate the miles per gallon based on user input. Store the list of trips in a csv file and display the contents.
#
# Associated file: trips.csv
#
# Note: Referenced the example from workshop for parts of lab

# Insert in the output student's name and exact date/time lab was run.
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")

import csv # import csv module

TRIPSFILE = "trips.csv" # save trips.csv in global constant to use later

# ask the user for miles driven and validate input
def get_miles_driven():
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven

# ask the user for gallons used and validate input
def get_gallons_used():
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

# write the contents of the trips list to the trips.csv
def write_trips(trips):
    with open(TRIPSFILE, "w", newline="") as file:
        writer= csv.writer(file)
        writer.writerows(trips)

# read the contents of trips.csv and append the data to trips list
def read_trips():
    trips = []
    with open(TRIPSFILE, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            trips.append([float(row[0]), float(row[1]), float(row[2])])
    return trips

# display all trips
def display_trips(trips):
    if len(trips) > 0:
        print("Distance\tGallons\t\tMPG")
        for trip in trips:
            print(f"{trip[0]}\t\t{trip[1]}\t\t{trip[2]}")
        print()

# call all functions needed
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    trips = read_trips() 
    display_trips(trips) # display the trips list

    more = "y"
    while more.lower() == "y":
        # get user input
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()

        # calculate and display MPG                         
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        # append data to trip, then append trip to trips list
        trip = []
        trip.append(miles_driven)
        trip.append(gallons_used)
        trip.append(mpg)
        trips.append(trip)

        display_trips(trips) #display trips

        # ask user if they want to input more trips
        more = input("More entries? (y or n): ")
    
    write_trips(trips) # write the contents to trips.csv

    # say bye
    print("Bye!")

if __name__ == "__main__":
    main()

