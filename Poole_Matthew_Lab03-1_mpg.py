#!/usr/bin/env python3
#
# Matthew Poole, January 27, 2026, CPT127-424, Lab03-1
#
# Program: Enhanced Miles Per Gallon Application
# Purpose: Get the miles driven, gallons used, and cost per gallon
#          from the user and calculate the miles per gallon, total gas cost, and
#          cost per mile. Program gives the user the opportunity to repeat the code
#          by entering y or Y at the end, if anything else is entered, the program ends.
# Associated file(s): none

import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")

# display a welcome message
print("The Miles Per Gallon Program")
print()
# initialize choice as y so the loop runs the first time
choice = "y"

# loop will run as long as the user chooses to input "y" or "Y" at the end
while choice.lower() == "y":
    # get miles driven, gallons used, and cost per gallon as float variables
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    cost_per_gallon = float(input("Enter cost per gallon:      "))
    print()

    # Check if any of the values entered are less than zero, if so, display an
    # errror message, if not, move to calculations.
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif cost_per_gallon <= 0:
        print("Cost per gallon must be greater than zero. Please try again.")
    else:
        # calculate the miles per gallon, total gas cost, and cost per mile and
        # round them to 2 decimal places.
        mpg = round(miles_driven / gallons_used, 2)
        total_gas_cost = round(cost_per_gallon * gallons_used, 2)
        cost_per_mile =  round(total_gas_cost / miles_driven, 2)
        # print out results
        print(f'Miles Per Gallon:\t    {mpg}'
              f'\nTotal Gas Cost:\t\t    {total_gas_cost}'
              f'\nCost Per Mile:\t\t    {cost_per_mile}')
    print()
    # ask user if they want to repeat the code
    choice = input("Get entries for another trip (y/n)? ")
    print()
# say bye
print("Bye!")



