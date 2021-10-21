"""Practice with dictionaries."""

__author__ = "730330989"

# Define your functions below


def invert(a: dict[str, str]) -> dict[str, str]:
    """A function that will take in a dictionary and switch the keys with the values."""
    result: dict[str, str] = {}
    for key in a:
        if a[key] in result:
            raise KeyError("Error")
        else:
            result[a[key]] = key
    return result


def favorite_color(a: dict[str, str]) -> str:
    """Returns most frequent color in a dictionary."""
    counter: dict[str, int] = {}
    fav: str = ""
    colors: str
    for key in a:
        colors = a[key]
        if colors in counter:
            counter[colors] += 1
        else:
            counter[colors] = 1
    maximum: int = 0
    for colors in counter:
        if counter[colors] > maximum:
            maximum = counter[colors]
            fav = colors
    return fav


def count(a: list[str]) -> dict[str, int]:
    """Returns a dictionary with with counts of items in the input list."""
    empty: dict[str, int] = {}
    count: str = ""
    for count in a:
        if count in empty:
            empty[count] += 1
        else:
            empty[count] = 1
    return empty