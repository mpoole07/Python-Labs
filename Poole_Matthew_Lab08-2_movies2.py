#!/usr/bin/env python3
#
# Matthew Poole, March 10, 2026, CPT127-424, Lab08-2
#
# Program: Movie List Program
# Purpose: Allow user to print, add, or remove movies from a list that is stored in a movies_test.csv file. 
#
# Associated file(s): movies_test.csv

# Insert in the output student's name and exact date/time lab was run.
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")
print()

# import csv and sys modules
import csv
import sys

# initialize global constant FILENAME as movies_test.csv file
FILENAME = "movies_test.csv"

# end the program
def exit_program():
    print("Terminating program.")
    sys.exit()

# read contents of the movies_test.csv file and append to movies list
def read_movies():
    try:
        movies = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except FileNotFoundError as e:
        #print(f"Could not find {FILENAME} file.")
        #exit_program()
        return movies
    except Exception as e:
        print(type(e), e)
        exit_program()

# write movies list to the movies_test.csv file
def write_movies(movies):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(movies)
            #raise BlockingIOError("BlockingIOError test")
    except OSError as e:
        print(type(e), e)
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()
# print a list of all movies in the list including the number and year
def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie[0]} ({movie[1]})")
    print()

# allow the user to add a movie to the list by inputting the name and year
def add_movie(movies):
    name = input("Name: ")
    while True:
        year = int(input("Year: "))
        if year < 1: # make sure year entered is not 0 or below
            print("Invalid year. Please try again.")
        else:
            break
    movie = [name, year]
    movies.append(movie) # add movie to list
    write_movies(movies) # save new list to the csv file
    print(f"{name} was added.\n")

# allow user to delete movie from the list by entering the movie's corresponding number
def delete_movie(movies):
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Invalid number. Please try again. Example: 1, 2, 3")
            continue
        if number < 1 or number > len(movies):
            print("There is no movie with that number. Please try again.")
        else:
            break
    movie = movies.pop(number - 1)
    write_movies(movies)
    print(f"{movie[0]} was deleted.\n")

# display the command menu
def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

# call all functions needed based on user's command
def main():
    display_menu()
    movies = read_movies()
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

# if we are in main run main()
if __name__ == "__main__":
    main()
