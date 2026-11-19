#!/usr/bin/env python3
# Matthew Poole, January 22, 2026, CPT127-424, Lab02-3
# Program: Area and Perimeter Program
# Purpose: Get the length and width of a rectangle from the user
#          and calculate the area and the perimeter.

import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")

# display a welcome message
print("The Area and Perimeter program")
print()

# get input from the user of the length and width
length = float(input("Enter the length:\t"))
width = float(input("Enter the width:\t"))

# calculate the area and perimeter
area = round(length * width, 2)
perimeter = round((width * 2) + (length * 2), 2)
            
# display the area and perimeter
print()
print(f"Area = {area}"
      f"\nPerimeter = {perimeter}")
print()
print("Bye!")


