"""Testing our dictionary functions."""

__author__: str = "730560378"


import pytest
from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count

with pytest.raises(KeyError):
    """Testing to see if key error is raised if duplicate elems."""
    my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
    invert(my_dictionary)


def test_invert_names() -> None:
    """Testing if invert works for dict of first and last names."""
    test_dict: dict[str, str] = {"Alexander": "Hamilton", "Brady": "Rassin", "Symere": "Woods"}
    assert invert(test_dict) == {"Hamilton": "Alexander", "Rassin": "Brady", "Woods": "Symere"}


def test_invert_empty() -> None:
    """Testing if invert returns an empty dict when given one."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_characters() -> None:
    """Testing if invert works for dict of characters."""
    test_dict: dict[str, str] = {"a": "b", "c": "d", "e": "f", "g": "h"}
    assert invert(test_dict) == {"b": "a", "d": "c", "f": "e", "h": "g"}


def test_favorite_color_normal() -> None:
    """Testing if favorite_colors works for a sample dictionary."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_tie() -> None:
    """Testing if favorite_colors returns the first color when there is a tie."""
    test_dict: dict[str, str] = {"Fred": "orange", "Scooby": "yellow", "Velma": "orange", "Shaggy": "yellow"}
    assert favorite_color(test_dict) == "orange"


def test_favorite_color_one_person() -> None:
    """Testing if favorite_colors returns the favorite color if there's only one entry in dictionary."""
    test_dict: dict[str, str] = {"Margo": "Red"}
    assert favorite_color(test_dict) == "Red"


def test_count_empty() -> None:
    """Testing if count returns an empty dictionary if given an empty dictionary."""
    test_list: list[str] = []
    assert count(test_list) == {}


def test_count_no_repeats() -> None:
    """Testing if count returns a dict with all values of 1 if there are no repeats."""
    test_list: list[str] = ["apple", "banana", "canteloupe", "dragonfruit"]
    assert count(test_list) == {"apple": 1, "banana": 1, "canteloupe": 1, "dragonfruit": 1}


def test_count_multiple_repeats() -> None:
    """Testing if count can correctly count multiple repeats of multiple variables."""
    test_list: list[str] = ["A", "B", "A-", "A", "B", "A", "C", "A"]
    assert count(test_list) == {"A": 4, "A-": 1, "B": 2, "C": 1}