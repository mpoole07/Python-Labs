#!/usr/bin/env python3
#
# Matthew Poole, February 20, 2026, CPT127-424, Lab06-1
#
# Program: Test Scores Application
# Purpose: Calculate and display the total score, number of scores, average score, low score,
#          high score, and median score based on the user's input of test scores
#
# Associated file(s): none

# insert in the output student's name and exact date/time lab was run
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")
print()

# display welcome message
def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

# get and validate the scores and return them to main
def get_scores():
    scores = [] # declare scores as a list
    while True:
        score = input("Enter test score: ") # ask for user input
        if score == "x": # return scores when 'x' is entered
            return scores
        else: 
            score = int(score) # turn score into int
            if score >= 0 and score <= 100: # verify score is within range
                scores.append(score) # add the score to the end of the list
            else:
                print("Test score must be from 0 through 100. " + # tell the user score is invalid
                      "Score discarded. Try again.")

# calculate and display values
def process_scores(scores):
    score_total = 0
    for score in scores:
        score_total += score # add each score in scores together to get a total
    count = len(scores) # finds how many scores in list and adds them to count variable
    average = score_total / count #calculate the average
    low_score = min(scores) # find the lowest score
    high_score = max(scores) # find the highest score
    scores.sort() # sort the scores so the median can be calculated
    
    # checks if the # of scores is even or odd and calculates the median accordingly
    # (ChatGPT used to help with the median calculation section)
    mid = count // 2
    if count % 2 == 0:
        median_score = (scores[mid - 1] + scores[mid]) / 2
    else:
        median_score = scores[mid]
                
    # format and display the results
    print()
    print("Score total:       ", score_total)
    print("Number of Scores:  ", count)
    print("Average Score:     ", average)
    print("Low Score:         ", low_score)
    print("High Score:        ", high_score)
    print("Median Score:      ", median_score)

def main():
    # call all functions to run the program
    display_welcome()
    scores = get_scores()
    process_scores(scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


