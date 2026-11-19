#!/usr/bin/env python3
#
# Matthew Poole, April 14, 2026, CPT127-424, Lab12-1
#
# Program: Book Catalog Program
# Purpose: Create a dictionary containing books with details such as the author
#          and publication year. Allow the user to add, remove, edit, or search
#          from the books
#
# Associated file(s): none

# Insert in the output student's name and exact date/time lab was run.
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")
print()

# allows the user to search for a book based on its title and returns the author and pub year
def show_book(book_catalog):
    title = input("Title: ")
    if title in book_catalog:
        book = book_catalog[title]
        print(f"Title:    {title}")
        print(f"Author:   {book['author']}")
        print(f"Pub year: {book['pubyear']}")
    else:
        print(f"Sorry, {title} doesn't exist in the catalog.")

# list all books in the dictionary
def list_books(book_catalog):
    if len(book_catalog) > 0:
        for book in book_catalog:
            print()
            print(f"Title:    {book}")
            print(f"Author:   {book_catalog[book]['author']}")
            print(f"Pub year: {book_catalog[book]['pubyear']}\n")
    else:
        print("There are no books in the catalog.") # if there aren't any books display this message
        

# add or edit a book based on the mode which is assigned as either "add" or "edit" when the function is called
def add_edit_book(book_catalog, mode):
    title = input("Title: ")
    if mode == "add" and title in book_catalog:
        print(f"{title} already exists in the catalog.")
        response = input ("Would you like to edit it? (y/n): ").lower()
        if(response != "y"):
            return
    elif mode == "edit" and title not in book_catalog:
        print(f"{title} doesn't exist in the catalog.")
        response = input("Would you like to add it? (y/n): ").lower()
        if (response != "y"):
            return

    # Get remaining book data and create a dictionary for the data
    author = input("Author name: ")
    pubyear = input("Publication year: ")
    book = {title: {"author": author, "pubyear": pubyear}}

    # Add the book data to the catalog using the update operator
    book_catalog |= book

# delete a book from the catalog
def delete_book(book_catalog):
    title = input("Title: ")
    if title in book_catalog:
        del book_catalog[title]
        print(f"{title} removed from catalog.")
    else:
        print(f"{title} doesn't exist in the catalog.")

# display the command menu
def display_menu():
    print("The Book Catalog program")
    print()
    print("COMMAND MENU")
    print("list - List all books")
    print("show - Show book info")
    print("add -  Add book")
    print("edit - Edit book")
    print("del -  Delete book")
    print("exit - Exit program")

def main():
    display_menu()
    book_catalog = { # initialize the book catalog dictionary with 3 books
        "Moby Dick": 
            {"author" : "Herman Melville",
             "pubyear" : "1851"},
        "The Hobbit":
            {"author" : "J. R. R. Tolkien", 
             "pubyear" : "1937"},
        "Slaughterhouse Five":
            {"author" : "Kurt Vonnegut",
             "pubyear" : "1969"}
        }
    # take users command input and call the proper function
    while True:
        print()
        command = input("Command: ").lower()
        if command == "show":
            show_book(book_catalog)
        elif command == "list":
            list_books(book_catalog)
        elif command == "add":
            add_edit_book(book_catalog, mode="add")
        elif command == "edit":
            add_edit_book(book_catalog, mode="edit")
        elif command == "del":
            delete_book(book_catalog)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
