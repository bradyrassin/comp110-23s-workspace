"""Making dictionary with strings of first list and int's of second list."""

def zip(first_list: list[str], second_list: list[int]):
    """Dict with strings of first list and int's of second."""
    combined_dict: dict(str, int) = {}
    if len(first_list) != len(second_list):
        return combined_dict
    if len(first_list) and len(second_list) == 0:
        return combined_dict
    for idx in range(0, len(first_list)):
        combined_dict[first_list[idx]] = second_list[idx]
    return combined_dict