def count_charcaters(given: str) -> dict[str, int]:
    """Counts how many times each character appears in the given string.

    This is just some example. It's not important what it does.

    :param given: The string to inspect.
    """
    result: dict[str, int] = {}
    for character in given:
        if character not in result:
            result[character] = 1
        else:
            result[character] += 1
    return result
