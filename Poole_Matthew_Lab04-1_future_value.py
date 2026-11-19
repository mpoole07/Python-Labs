#!/usr/bin/env python3
#
# Matthew Poole, February 8, 2026, CPT127-424, Lab04-1
#
# Program: Future Value Calculator
# Purpose: Calculate and display the future value of an investment based on 3 validated user inputs
#
# Associated file(s): none

# insert in the output student's name and exact date/time lab was run
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")

print()
# display welcome message
print("Welcome to the Future Value Calculator")
print()

# import validation module so it can be used later
import validation

# function accepts monthly investment, yearly interest and years as inputs assuming they have already
# been properly validated
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

# function that runs the whole program and can loop
def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        # gets and validates the monthly investment using the get_float function in the validation module
        monthly_investment = validation.get_float("Enter monthly investment:\t", 0, 1000)
        # gets and validates the yearly interest rate using the get_float function in the validation module
        yearly_interest_rate = validation.get_float("Enter yearly interest rate:\t", 0, 15)
        # gets and validates the number of years using the get_int function in the validation module
        years = validation.get_int("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print()
        # prints future value rounded to 2 decimals places
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
