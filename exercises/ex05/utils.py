"""List utility functions part 2."""

__author__ = "730330989"

# Define your functions below


def only_evens(xs: list[int]) -> list[int]:
    """This is a function that when given a list of ints will return the even ints."""
    # run through the list
    i: int = 0
    ys: list[int] = list()
    while i < len(xs):
        if xs[i] % 2 == 0:
            ys.append(xs[i])
        i += 1
    return ys


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """A function that takes a list, a start index and a end index that returns a list that is a subset of the one given, between the specified start index and end index -1."""
    ys: list[int] = list()
    if len(xs) == 0:
        return xs
    if start < 0:
        start = 0
    if end > len(xs):
        end = len(xs) - 1
    while start < end:
        ys.append(xs[start])
        start += 1
    return ys


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Function that inputs two lists, and outputs a list containing all the elements of the first list followd by the elements of the second list."""
    i: int = 0
    j: int = 0
    zs: list[int] = list()
    while i < len(xs):
        zs.append(xs[i])
        i += 1
    while j < len(ys):
        zs.append(ys[j])
        j += 1
    return zs