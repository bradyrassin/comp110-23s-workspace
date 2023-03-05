"""Unit tests for util functions."""

__author__ = "730560378"

from exercises.ex05_utils import only_evens, sub, concat

def test_empty() -> None:
    """Testing only_evens when given empty list."""
    assert only_evens([]) == []

def test_multiple_evens() -> None:
    """Testing only_evens when given a list of multiple evens."""
    assert only_evens([2, 2, 4, 4, 6, 8]) == [2, 2, 4, 4, 6, 8]

def test_mixed_list() -> None:
    """Testing if only_evens works for a mixed list."""
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]

def test_one_empty() -> None:
    """Testing concat when one of the lists given is empty."""
    assert concat([], [1, 2, 3]) == [1, 2, 3]

def test_one_int_lists() -> None:
    """Testing concat when given two lists, one int long."""
    assert concat([1], [2]) == [1, 2]

def test_longer_lists() -> None:
    """Testing concat function with two longer lists."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]

def test_greater_start_index() -> None:
    """Testing sub when given a greater start index than length of list."""
    assert sub([1, 2, 3], 4, 6) == []

def test_two_numbers() -> None:
    """Testing sub function with a list of 2 numbers long."""
    assert sub([1, 2], 0, 1) == [1]

def test_long_list() -> None:
    """Testing sub function with a longer list."""
    assert sub([1, 2, 3, 4, 5], 0, 4)