#!/usr/bin/env python3
#
# Matthew Poole, February 20, 2026, CPT127-424, Lab06-2
#
# Program: Movie List Program
# Purpose: Provide a list of movies containing the title, year, and price, and allow users to
#          add, find, or delete movies on the list.
#
# Associated file(s): none

# insert in the output student's name and exact date/time lab was run
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")
print()

def list(movie_list):
    if len(movie_list) == 0: # check if there are no movies in the list
        print("There are no movies in the list.\n")
        return
    else:
        for i, movie in enumerate(movie_list, start=1): # go through each movie in list and print out each column
            print(f"{i}. {movie[0]} ({movie[1]}) @ {movie[2]}")
        print()

def add(movie_list):
    # ask the user to input the name, year and price of movie
    name = input("Name: ")
    year = int(input("Year: "))
    price = input("Price: ")
    movie = [name, year, price]
    movie_list.append(movie) # add movie to the movie list
    print(f"{movie[0]} was added.\n")
    
def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list): # check to make sure number actually exists in the list
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1) # delete the movie from the list
        print(f"{movie[0]} was deleted.\n")

def find(movie_list):
    year = int(input("Year: "))
    count = 0 # initialize as 0 so it can be added onto when a movie is found
    for movie in movie_list:
        if movie[1] == year: # go through each movie in movie_list and check if the year matches
            print(f"{movie[0]} was released in {movie[1]}.")
            count += 1
    if count == 0: # if count == 0, no movies were found so send this message to tell the user
        print(f"There are no movies in the list that were released in {year}.")

# display a list of commands
def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("find - Find a movie")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()
    
def main():
    # initialize the movie list with these 3 movies
    movie_list = [["Monty Python and the Holy Grail", 1975, 9.95],
                  ["On the Waterfront", 1954, 5.59],
                  ["Cat on a Hot Tin Roof", 1958, 7.95]]
    
    display_menu()
    # call each function based on the command entered
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list(movie_list)
        elif command.lower() == "add":
            add(movie_list)
        elif command.lower() == "del":
            delete(movie_list)
        elif command.lower() == "find":
            find(movie_list)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
