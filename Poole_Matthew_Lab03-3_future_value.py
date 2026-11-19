#!/usr/bin/env python3
#
# Matthew Poole, February 1, 2026, CPT127-424, Lab03-2
#
# Program: Future Value Calculator
# Purpose: Ask the user to input the amount of monthly investment, yearly interest rate, and amount of years
#          then validate those values to make sure they are reasonable. Program will then calculate the monthly
#          interest rate and the amount of months and then calculate the future value using a for loop.
#          Using an if statement the program displays the future value every year for the amount of years the
#          user entered.
# Associated file(s): none

# insert in the output student's name and exact date/time lab was run
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

# set choice equal to string "y"
choice = "y"

# while loop will run as long as choice equals "y" or "Y"
while choice.lower() == "y":

    # get the monthly investment as input from the user, then validate it
    while True:
        monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment < 1:
            print("Entry must be greater than 0. Please try again.")
        else:
            break

    # get the yearly interest rate from the user, then validate it
    while True:
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        if yearly_interest_rate < 1 or yearly_interest_rate > 15:
            print("Entry must be greater than 0 and less than or equal to 15. Please try again.")
        else:
            break

    # get the years from the user, then validate it
    while True:
        years = int(input("Enter number of years:\t\t"))
        if years < 1 or years > 50:
            print("Entry must be greater than 0 and less than or equal to 50. Please try again.")
        else:
            break

    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest_rate / 12 / 100 # also converts to a decimal for calculations
    months = years * 12

    # calculate the future value
    future_value = 0
    print()
    for i in range(months):
        # adds the monthly investment to the future value, then calculates the 
        # monthly interest amount and adds that to the future value as well
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount
        # determines if it is a whole year and if so displays the future value for that year
        if (i+1) % 12 == 0:
            print(f"Year =  {(i+1) // 12}\t Future Value = {round(future_value, 2)}")

    # see if the user wants to continue
    print()
    choice = input("Continue (y/n)? ")
    print()

# say bye
print("Bye!")
