def short_words(list1: list[str]) -> list[str]:
    """Stuftt"""
    idx: int = 0
    new_list: list[str] = []
    while idx < len(list1):
        if len(list1[idx]) < 5:
            new_list.append(list1[idx])
        else:
            print(f"{list1[idx]} is too long!")
        idx += 1
    return new_list
