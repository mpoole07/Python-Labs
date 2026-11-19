#!/usr/bin/env python3
#
# Matthew Poole, April 14, 2026, CPT127-424, Lab12-2
#
# Program: Movie List Program
# Purpose: Create a movie list containing the name and year of the movie. Allow user to add or delete movies from the dictionary.
#
# Associated file(s): none

# Insert in the output student's name and exact date/time lab was run.
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")
print()

# list the movies from the dictionary
def list(movie_list):
    if len(movie_list) == 0:
        print("There are no movies in the list.\n") 
        return
    else:
        for i, movie in enumerate(movie_list, start=1):
            print(f"{i}. {movie['name']} ({movie['year']})") # Changed so that it displays the movie name and year from the dictionary
        print()

# add a movie to the list
def add(movie_list):
    name = input("Name: ")
    year = input("Year: ")
    movie = {"name": name, "year": year} # changed so that the name and year both correspond to the "name" and "year" keys in the dictionary.
    movie_list.append(movie)
    print(f"{movie['name']} was added.\n") # changed to get the name from the dictionary using the "name" key

# delete a movie from the list
def delete(movie_list):
    number = int(input("Number: "))
    if number < 1 or number > len(movie_list):
        print("Invalid movie number.\n")
    else:
        movie = movie_list.pop(number-1)
        print(f"{movie['name']} was deleted.\n") # changed to get the name from the dictionary using the "name" key

# print the command menu
def display_menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()

# call all required functions to run the program        
def main():
    # changed movie list to a dictionary with "name" and "year" keys corresponding to the name and year
    movie_list = [{"name": "Monty Python and the Holy Grail", "year": 1975},
                  {"name": "On the Waterfront", "year": 1954},
                  {"name": "Cat on a Hot Tin Roof", "year": 1958}]
    
    display_menu()

    # get the user's command input and call the correct function
    while True:        
        command = input("Command: ")
        if command == "list":
            list(movie_list)
        elif command == "add":
            add(movie_list)
        elif command == "del":
            delete(movie_list)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
