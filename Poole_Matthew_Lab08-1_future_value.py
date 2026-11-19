#!/usr/bin/env python3
# Matthew Poole, March 10, 2026, CPT127-424, Lab08-1
#
# Program: Future Value Program
# Purpose: Calculate the future value of an investment based on the user's input of monthly investment, yearly interest rate, and number of years.
#
# Associated file(s): none

# Insert in the output student's name and exact date/time lab was run.
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")
print()

# ask the user for a number as input, accepting a prompt, a low, and a high as arguments.
def get_number(prompt, low, high):
    while True:
        try:
            number = float(input(prompt))
        except ValueError: # if user enters the wrong value type, print message and try again.
            print("Entry must be a number. Please try again.")
            continue
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print(f"Entry must be greater than {low} " 
                  f"and less than or equal to {high}.")

# ask the user for an integer as input, accepting a prompt, a low, and a high as arguments.
def get_integer(prompt, low, high):
    while True:
        try:
            number = int(input(prompt))
        except ValueError: # if user enters the wrong value type, print message and try again.
            print("Entry must be a whole number. Please try again.")
            continue
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print(f"Entry must be greater than {low} " 
                  f"and less than or equal to {high}.")

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

# call all functions for the program
def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_number("Enter yearly interest rate:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        
        print()
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")

# if the current module is main, run main()
if __name__ == "__main__":
    main()
