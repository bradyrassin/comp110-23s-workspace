"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = 730560378

chosen_word: str = input("Enter a 5-character word: ")

chosen_letter: str = input("Enter a single character: ")

print("Searching for " + chosen_letter + " in " + chosen_word)

matched_letter = 0

if (chosen_word[0] == chosen_letter):
    print (chosen_letter + " found at index 0")
    matched_letter += 1

if (chosen_word[1] == chosen_letter):
    print (chosen_letter + " found at index 1")
    matched_letter += 1

if (chosen_word[2] == chosen_letter):
    print (chosen_letter + " found at index 2")
    matched_letter += 1

if (chosen_word[3] == chosen_letter):
    print (chosen_letter + " found at index 3")
    matched_letter += 1

if (chosen_word[4] == chosen_letter):
    print (chosen_letter + " found at index 4")
    matched_letter += 1

if (matched_letter == 0):
    print ("No instances of " + chosen_letter + " found in " + chosen_word)
if (matched_letter == 1):
    print ("1 instance of " + chosen_letter + " found in " + chosen_word)
if (matched_letter >= 2):
    print (str(matched_letter) + " instances of " + chosen_letter + " found in " + chosen_word)