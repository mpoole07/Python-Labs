#!/usr/bin/env python3
#
# Matthew Poole, February 14, 2026, CPT127-424, Lab05-1
#
# Program: Test Scores Application
# Purpose: Calculate and display the average and total score based on the user's input
#
# Associated file(s): none

# insert in the output student's name and exact date/time lab was run
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")

# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter 'x' to end input")
print("======================")

# initialize variables
counter = 0
score_total = 0
test_score = 0

# run the user input for test score
while True:
    try:
        # give user instructions on what to input
        test_score = input("Enter test score (or 'x' to quit): ")
        # see if user entered 'x' and if so break out of loop
        if test_score == "x":
            break
        else:
            test_score = int(test_score) # convert test_score variable to int
            # check if score is within proper range
            if test_score >= 0 and test_score <= 100:
                # add score to total and add one to counter
                score_total += test_score
                counter += 1
            else:
                # tell the user their number isn't in range
                print("Test score must be from 0 through 100. Score discarded. Try again.")
    except:
        # if the user enters anything that isn't a integer or 'x', this will pop up
        print("Please enter a whole number between 0 and 100. Try again.")

# check to see if the user actually entered any numbers to prevent dividing by zero error
if counter == 0:
    print("No numbers were entered so no calculations could be made.")
else:
    # calculate the average score
    average_score = round(score_total / counter)
    # format and display the result
    print("======================")
    print(f"Total Score: {score_total}"
          f"\nAverage Score: {average_score}")
                
print()
print("Bye")


