"""Creating a real wordle"""
__author__ = "730560378"

def contains_char(chosen_word: str, matching_letter: str) -> bool:
    """Checks given word to see if letter is in it"""
    assert len(matching_letter) == 1
    idx: int = 0
    while idx < len(chosen_word):
        if chosen_word[idx] == matching_letter:
            return True
        else:
            idx = idx + 1
    return False

def emojified(guess_word: str, secret_word: str) -> str:
    """Checks indexes and gives colored box response"""
    assert len(guess_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    idx: int = 0
    result: str = ""
    while idx < len(secret_word): #checking each index and adding to result
        if guess_word[idx] == secret_word[idx]:
            result = result + GREEN_BOX
        else:
            if contains_char(secret_word, guess_word[idx]) == True:
                result = result + YELLOW_BOX
            else: 
                result = result + WHITE_BOX
        idx = idx + 1
    return result

def input_guess(expected_length: int) -> str:
    """Prompts user for word of expected length"""
    guess_word: str = input(f"Enter a {expected_length} character word: ")
    if len(guess_word) == expected_length:
        return guess_word
    else: #if the length is incorrect
        new_guess: str = input(f"That wasn't {expected_length} chars! Try again: ")
        while len(new_guess) != expected_length:
            new_guess = input(f"That wasn't {expected_length} chars! Try again: ")
        return new_guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    win_status: bool = False
    n: int = 1
    while n <= 6 and not win_status: #Guess counter that gives prompts
        print(f"=== Turn {n}/6 ===")
        guess: str = input_guess(5)
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {n}/6 turns!")
            win_status = True
        n = n + 1
    if n >= 7:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()