#!/usr/bin/env python3
#
# Matthew Poole, April 5, 2026, CPT127-424, Lab10-2
#
# Program: Word Counter Program
# Purpose: Count the number of sentences, words, and unique words in a text file.
#
# Associated file(s): gettysburg_address.txt

# Insert in the output student's name and exact date/time lab was run.
import datetime
print(f"Student Name: Matthew Poole")
labtime = datetime.datetime.now()
print(f"Lab Time: {labtime}")
print()

# get the number of words in the file then return
def get_words_from_file(filename):
    with open(filename) as file:
        text = file.read()    # read str from file

    # print(text)
    text = text.replace("\n", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.lower()
    
    words = text.split(" ")   # convert str to list
    words.sort()
    # print(words)
    return words

# find unique words and find out how many times they appear
def get_unique_words(words):
    unique_words = []
    unique_words.append(words[0])
    
    for i in range(1, len(words)):
        if words[i] == words[i - 1]:
            continue
        else:
            unique_words.append(words[i])            
    return unique_words

# find the number of sentences by splitting the text into a list for each appearance of "." 
def get_sentences(filename):
    with open(filename) as file:
        text = file.read()
    sentences = text.split(".")
    return sentences

def main():
    filename = "gettysburg_address.txt" # initialize filename variable as gettysburg address text file
    print("The Word Counter program\n")  

    # get words and unique words
    words = get_words_from_file(filename) # get list of words
    unique_words = get_unique_words(words)
    sentences = get_sentences(filename) # get # of sentences

    # display number of words and unique words
    print(f"Number of sentences = {len(sentences)}")
    print(f"Number of words = {len(words)}")
    print(f"Number of unique words = {len(unique_words)}")

    # display unique words and their word counts
    print("Unique word occurrences:")
    for word in unique_words:
        print(f"    {word} = {words.count(word)}")
 
if __name__ == "__main__":
    main()
