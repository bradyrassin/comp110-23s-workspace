"""Implementing algorithms to practice computational thinking"""
__author__ = "730560378"

def all(given_list: list[int], given_number: int) -> bool:
    """Checks given list to see if all the numbers in the list match the given number"""
    i: int = 0
    while i < len(given_list):
        if given_list[i] != given_number:
            return False
        else:
            i += 1
    return True

def max(input: list[int]) -> int:
    """Return Max Number from List"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    maximum: int = ""
    if input[0] >= input[1]:
        maximum = input[0]
    else:
        maximum = input[1]
    idx: int = 2
    while idx < len(input):
        if input[idx] > maximum:
            maximum = input[idx]
        idx += 1
    return maximum

def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Checks both lists for deep equality"""
    if len(first_list) != len(second_list):
        return False
    idx: int = 0
    while idx < len(first_list):
        if first_list[idx] != second_list[idx]:
            return False
        else:
            idx += 1
    return True
    
