#!/usr/bin/env python3
#
# Matthew Poole, April 5, 2026, CPT127-424, Lab10-1
#
# Program: Create Account Program
# Purpose: Create an account for a user including their full name, email, phone number, and a password
#
# Associated file(s): none

# Insert in the output student's name and exact date/time lab was run.
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")
print()

# call all functions and display confirmation message at the end
def main():
    full_name = get_full_name()
    print()
    
    password = get_password()
    print()

    email = get_email()
    print()

    number = get_number()
    print()
    
    first_name = get_first_name(full_name)   
    print(f"Hi {first_name}, thanks for creating an account.")
    print(f"We'll text your confirmation code to this number: {number}")

# ask user for full name, then confirm it is a full name by checking for a space in the middle
def get_full_name():
    while True:
        name = input("Enter full name:       ").strip() # remove unnecessary spaces with strip
        if " " in name:
            return name
        else:
            print("You must enter your full name.")

# find the first name by seeing where the space is and then put the characters before that index in a first_name variable
def get_first_name(full_name):
    index1 = full_name.find(" ")
    first_name = full_name[:index1]
    return first_name

# ask the user to enter valid password with at least 8 characters, a digit, and an uppercase letter
def get_password():
    while True:
        digit = False
        cap_letter = False
        password = input("Enter password:        ").strip()
        for char in password:
            if char.isdigit():
                digit = True
            elif char.isupper():
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8:
            print(f"Password must be 8 characters or more \n"
                  f"with at least one digit and one uppercase letter.")
        else:
            return password

# ask user to enter email and confirm it has "@" and ends with ".com"
def get_email():
    while True:
        email = input("Enter email address:   ").strip()
        if "@" in email and email.endswith(".com"):
            return email
        else:
            print("Please enter a valid email address.")

# ask user to enter phone number and remove any unnecessary characters, then validate the number's length and format it with periods
def get_number():
    while True:
        number = input("Enter phone number:    ").strip()
        for char in number:
            if char in " -().":
                number = number.replace(char, "")
        if len(number) == 10 and number.isdigit():
            number = number[0:3] + "." + number[3:6] + "." + number[6:]
            return number
        else:
            print("Please enter a 10-digit phone number.")
        
if __name__ == "__main__":
    main()
