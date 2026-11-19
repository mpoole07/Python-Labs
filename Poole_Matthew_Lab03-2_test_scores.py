#!/usr/bin/env python3
#
# Matthew Poole, February 1, 2026, CPT127-424, Lab03-2
#
# Program: Test Scores Application
# Purpose: Ask the user to enter test scores and calculate the total score and average score.
#          The user can input as many scores as he/she wants and can type "end" when finished.
#          The program validates whether the user is inputting a valid number and will display
#          an error message if they are not. User can also choose to input another set of scores
#          by entering "y" or "Y" at the end.
# Associated file(s): none

# insert in the output student's name and exact date/time lab was run
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")

# display a welcome message
print("The Test Scores application")
print()

# initialize choice as string "y"
choice = "y"

# while loop will repeat if user enters "y" or "Y" at the end and allow them to enter a new set of scores
while choice.lower() == "y":
    # give user instructions on how to use and end program
    print("Enter test scores")
    print("Enter 'end' to end input")
    print("======================")
    # initialize counter, test_score, and score_total as zero
    counter = 0
    test_score = 0
    score_total = 0
    # while loop will ask for input, test if the user typed "end," and then move to validate the score and
    # either display an error message or add the score to the total
    while True:
        test_score = input("Enter test score: ")
        if test_score.lower() == "end": # see if user entered end, ignoring capitalization
            break # end loop and go to calculations
        else:
            test_score = int(test_score) # test_score is automatically a string, so it needs to be converted to int
            if test_score >= 0 and test_score <= 100: # test if the score is between 0 and 100
                score_total += test_score # add to the score total
                counter += 1 # add one to the counter for average calculations at the end
            else:
                print(f"Test score must be from 0 through 100. " # displays if score is not within proper range
                      f"Score discarded. Try again.")
    # calculate average score
    average_score = round(score_total / counter)
                    
    # format and display the results
    print("======================")
    print(f"Total Score: {score_total}"
          f"\nAverage Score: {average_score}")
    print()

    # ask user whether they want to input another set of scores
    # if anything other than "y" or "Y" is entered the program will end
    choice = input("Enter another set of test scores (y/n)?")
    
print()
# say bye
print("Bye!")


