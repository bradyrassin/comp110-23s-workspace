"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = 730560378

chosen_word: str = input("Enter a 5-character word: ")

chosen_letter: str = input("Enter a single character: ")

print("Searching for " + chosen_letter + " in " + chosen_word)

if (chosen_word[0] == chosen_letter):
    print (chosen_letter + " found at index 0")

if(chosen_word[1] == chosen_letter):
    print (chosen_letter + " found at index 1")

if(chosen_word[2] == chosen_letter):
    print (chosen_letter + " found at index 2")

if(chosen_word[3] == chosen_letter):
    print (chosen_letter + " found at index 3")

if(chosen_word[4] == chosen_letter):
    print (chosen_letter + " found at index 4")