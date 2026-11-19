#!/usr/bin/env python3
#
# Matthew Poole, April 5, 2026, CPT127-424, Lab10-3
#
# Program: Hangman Program
# Purpose: User has to guess a randomly chosen word by guessing one letter at a time.
#
# Associated file(s): none

# Insert in the output student's name and exact date/time lab was run.
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")
print()

import wordlist #import the words to be randomly chosen from

# Get a random word from the word list
def get_word():
    word = wordlist.get_random_word()
    return word.upper()

# Add spaces between letters
def add_spaces(word):
    word_with_spaces = " ".join(word)
    return word_with_spaces

# Draw the display
def draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word):
    print("-" * 79)
    draw_hangman(num_wrong)
    print("Word:", add_spaces(displayed_word),
          "  Guesses:", num_guesses,
          "  Wrong:", num_wrong,
          "  Tried:", add_spaces(guessed_letters))

# Get next letter from user
def get_letter(guessed_letters):
    while True:
        guess = input("Enter a letter: ").strip().upper()
    
        # Make sure the user enters a letter and only one letter
        if guess == "" or len(guess) > 1:
            print("Invalid entry. ",
                  "Please enter one and only one letter.")
            continue
        # Don't let the user try the same letter more than once
        elif guess in guessed_letters:
            print("You already tried that letter.")
            continue
        else:
            return guess

# draw the hangman according to the number of wrong guesses
# note: referenced solutions file for this function
def draw_hangman(num_wrong):
    if num_wrong == 1:
        print("_____")
        print("     |")
        print("     o")
    elif num_wrong == 2:
        print("_____")
        print("     |")
        print("     o")
        print("     |")
    elif num_wrong == 3:
        print("_____")
        print("     |")
        print("     o")
        print("    \\|")
    elif num_wrong == 4:
        print("_____")
        print("     |")
        print("     o")
        print("    \\|/")
    elif num_wrong == 5:
        print("_____")
        print("     |")
        print("     o")
        print("    \\|/")
        print("     |")
    elif num_wrong == 6:
        print("_____")
        print("     |")
        print("     o")
        print("    \\|/")
        print("     |")
        print("    /")
    elif num_wrong == 7:
        print("_____")
        print("     |")
        print("     o")
        print("    \\|/")
        print("     |")
        print("    / \\")
        

# The input/process/draw technique is common in game programming
def play_game():
    word = get_word()
    
    word_length = len(word) # identify length of the randomly chosen word
    remaining_letters = word_length
    displayed_word = "_" * word_length

    num_wrong = 0               
    num_guesses = 0
    guessed_letters = ""
    
    draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    # run the game until num_wrong = 7 or the word is completed
    while num_wrong < 7 and remaining_letters > 0:
        guess = get_letter(guessed_letters)
        guessed_letters += guess
        
        pos = word.find(guess, 0)
        if pos != -1:
            displayed_word = ""
            remaining_letters = word_length
            for char in word:
                if char in guessed_letters:
                    displayed_word += char
                    remaining_letters -= 1
                else:
                    displayed_word += "_"              
        else:
            num_wrong += 1

        num_guesses += 1

        draw_screen(num_wrong, num_guesses, guessed_letters, displayed_word)

    print("-" * 79)
    # see if user won or lost and display a message accordingly
    if remaining_letters == 0:
        print(f"Congratulations! You got it in {num_guesses} guesses.")   
    else:    
        print("Sorry, you lost.")
        print(f"The word was: {word}")

def main():
    print("Play the H A N G M A N game") #display title

    draw_hangman(7) # the 7 makes it print the full hangman, just at the beginning

    again = "y"
    while again.lower() == "y":
        play_game()
        print()
        again = input("Do you want to play again (y/n)?: ") #ask the user if they want to play again

    print("Bye!")

if __name__ == "__main__":
    main()
