"""One Shot Wordle using while loops"""

i: int = 0
result: str = "" #initialize to empty string

secret_word: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

chosen_word = input("What is your 6-letter word guess? ")

while (len(chosen_word) != 6): 
    chosen_word = input("That was not 6-letters! Try again: ")

while (i <= 5):
    if (chosen_word[i] == secret_word[i]):
        result = result + GREEN_BOX
    else:
        if (chosen_word[i] == secret_word[0]) or (chosen_word[i] == secret_word[1]) or (chosen_word[i] == secret_word[2]) or (chosen_word[i] == secret_word[3]) or (chosen_word[i] == secret_word[4]) or (chosen_word[i] == secret_word[5]):
            result = result + YELLOW_BOX
        else: 
            result = result + WHITE_BOX
    i = i + 1
print(result)
if chosen_word == secret_word:
    print("Woo! You got it!")
if chosen_word != secret_word:
    print("Not quite. Play again soon!")
