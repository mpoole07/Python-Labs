#!/usr/bin/env python3
#
# Matthew Poole, February 15, 2026, CPT127-424, Lab05-2
#
# Program: Future Value Calculator
# Purpose: Calculate and display the future value of an investment based on 3 validated user inputs
#
# Associated file(s): none
#
# insert in the output student's name and exact date/time lab was run
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")
print()

# accept a prompt, a low, and a high value as arguments to get a float input from the user and then validate
def get_float(prompt, low, high):
    while True:
        number = float(input(prompt))
        # make sure user input is within range
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            # send if user input is not within range
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.")

# accept a prompt, a low, and a high value as arguments to get an integer input from the user and then validate            
def get_integer(prompt, low, high):
    while True:
        number = int(input(prompt))
        # make sure user input is within range
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            # send if user input is not within range
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.")

# accept monthly investment, yearly interest, and number of years as arguments and then calculate and return future value
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 100 / 12
    #print("monthly interest rate: ", monthly_interest_rate)
    # convert years to months
    months = years * 12
    #print("months: ", months)

    future_value = 0.0
    # calculate future value
    for i in range(months-1):
        future_value += monthly_investment
        #print("future value: ", future_value)
        monthly_interest = future_value * monthly_interest_rate
        #print("Monthly interest: ", monthly_interest)
        future_value += monthly_interest
        #print("future value: ", future_value)

    return future_value

def main():
    choice = "y"
    # repeat code when the user chooses to
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_float("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_float("Enter yearly interest rate:\t", 0, 15)
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
    
if __name__ == "__main__":
    main()
