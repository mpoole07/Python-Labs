#!/usr/bin/env python3
# Matthew Poole, January 22, 2026, CPT127-424, Lab02-2
# Program requests input of 3 test scores from the user and adds them
# to a total score and calculates the average score and then displays them.

import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get three scores from the user and store them in three variables
score1 = int(input("Enter test score: "))
score2 = int(input("Enter test score: "))
score3 = int(input("Enter test score: "))
total_score = score1 + score2 + score3

# calculate average score
average_score = round(total_score / 3)
             
# format and display the scores and the results
print("======================")
print("Your Scores:  ", score1, score2, score3,
      "\nTotal Score:  ", total_score,
      "\nAverage Score:", average_score)
print()
print("Bye!")


