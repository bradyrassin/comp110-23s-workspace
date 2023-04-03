"""Setting up at the moment."""

__author__: str = "730560378"


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """Keys of the input list becomes the values of the output list and vice versa."""
    new_dict: dict[str, str] = {}
    for key in given_dict:
        new_dict[given_dict[key]] = key
    if len(new_dict) != len(given_dict):
        raise KeyError("Duplicate key encountered")
    return new_dict


def favorite_color(given_dict: dict[str, str]) -> str:
    """Return most frequent color, if tie return first in dictionary."""
    if len(given_dict) == 0:
        raise ValueError("Given dictionary is empty")
    tally_dict: dict[str, int] = {}
    for key in given_dict:
        color = given_dict[key]
        if color in tally_dict:
            tally_dict[color] += 1
        else:
            tally_dict[color] = 1
    color_name: str = ""
    color_tally: int = 0
    for key in tally_dict:
        if tally_dict[key] > color_tally:
            color_tally = tally_dict[key]
            color_name = key
    return color_name


def count(given_list: list[str]) -> dict[str, int]:
    """Counting how many times a value is in an input list."""
    new_dict: dict[str, int] = {}
    for elem in given_list:
        if elem in new_dict:
            new_dict[elem] += 1
        else:
            new_dict[elem] = 1
    return new_dict