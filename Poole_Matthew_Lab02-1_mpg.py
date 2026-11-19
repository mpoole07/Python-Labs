#!/usr/bin/env python3
# Matthew Poole, January 22, 2026, CPT127-424, Lab02-1
# Program takes input of miles driven, gallons of gas used, and gallon
# cost to calculate the MPG, total gas cost, and the cost per mile.

import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input of miles driven, gallons used, and gallon cost
# from user and turn it into float data type
miles_driven = float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
gallon_cost = float(input("Enter cost of a gallon of gas:\t"))

# calculate miles per gallon, the total gas cost, and the
# and the cost per mile and round to one decimal place.
mpg = round(miles_driven / gallons_used, 1)
gas_cost = round(gallon_cost * gallons_used, 1)
cost_per_mile = round(gas_cost / miles_driven, 1)
            
# format and display the results
print()
print(f"Miles Per Gallon:\t\t{mpg}")
print(f"Total Gas Cost:\t\t\t{gas_cost}")
print(f"Cost Per Mile:\t\t\t{cost_per_mile}")
print()
print("Bye!")


