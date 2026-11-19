#!/usr/bin/env python3
#
# Matthew Poole, April 7, 2026, CPT127-424, Lab11-1
#
# Program: Invoice Program
# Purpose: Calculate the due date of an invoice and amount of days until the due date based on the user's input of a date.
#
# Associated file(s): none

# Insert in the output student's name and exact date/time lab was run.
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")
print()

from datetime import datetime, timedelta, date

def get_invoice_date():
    while True:
        invoice_date_str = input("Enter the invoice date (MM/DD/YYYY): ") # ask user for invoice date in the proper format
        try:
            invoice_date = date.strptime(invoice_date_str, "%m/%d/%Y") # convert the string into date object
        except:
            # if theres a problem with the user's input that won't allow the string to be converted, show this message and restart loop
            print("Invalid date entered. Please enter a valid date such as 4/7/2026")
            continue
        # check to make sure the date given is either today or in the past
        if invoice_date > date.today():
            print(f"Please enter a date that is either today or in the past.")
        else:
            return invoice_date

def main():
    print("The Invoice Due Date program")
    print()

    again = "y"
    while again.lower() == "y":
        invoice_date = get_invoice_date() # call get_invoice_date() function to get date from user
        print()

        # calculate due date and days overdue
        due_date = invoice_date + timedelta(days=30) # add 30 days to the invoice date to get the due date
        current_date = date.today()
        days_overdue = (current_date - due_date).days # find how many days until the due date

        # display results
        date_format = "%B %d, %Y"
        print(f"Invoice Date: {invoice_date:{date_format}}")
        print(f"Due Date:     {due_date:{date_format}}")
        print(f"Current Date: {current_date:{date_format}}")
        if days_overdue > 0:
            print(f"This invoice is {days_overdue} day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print(f"This invoice is due in {days_due} day(s).")
        print()

        # ask if user wants to continue
        again = input("Continue? (y/n): ")
        print()
        
    print("Bye!")      

if __name__ == "__main__":
    main()
