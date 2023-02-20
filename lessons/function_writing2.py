def mimic_letter(my_words: str, letter_idx:int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx >= len(my_words):
        return("Index too high")
    #If we made it here, that means the letter_idx is valid
    else: 
        return (my_words[letter_idx])

