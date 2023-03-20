"""Building list utility functions continued."""


__author__ = "730560378"


def only_evens(numbers: list[int]) -> list[int]:
    """Given a list, return only the even numbers."""
    idx: int = 0
    even_list: list[int] = []
    while idx < len(numbers):
        if numbers[idx] % 2 == 0:
            even_list.append(numbers[idx])
        idx += 1
    return even_list


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Given two lists, return them as a single list."""
    combined_list: list[int] = []
    for element in list_one:
        combined_list.append(element)
    for element in list_two:
        combined_list.append(element)
    return combined_list


def sub(a_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Given a list, a start index and an end index return the numbers."""
    new_list: list[int] = []
    if len(a_list) == 0 or start_index >= len(a_list) or end_index <= 0:
        return new_list
    if start_index < 0:
        start_index = 0
    if end_index > len(a_list):
        end_index = len(a_list)
    for idx in range(start_index, end_index):
        new_list.append(a_list[idx])
    return new_list