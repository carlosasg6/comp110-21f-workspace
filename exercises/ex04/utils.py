"""List utility functions."""

__author__ = "730330989"


# TODO: Implement your functions here.


def all(xs: list[int], num: int) -> bool:
    """This is the all function, returning a bool True if all items in a list are the same as the num variable. Returns False if otherwise."""
    i: int = 0
    if len(xs) == 0:
        return False
    while i < len(xs):
        if xs[i] != num:
            return False
        i += 1
    return True


def is_equal(xs: list[int], ys: list[int]) -> bool:
    """Determines if two lists are deeply equal."""
    i: int = 0
    if len(xs) != len(ys):
        return False
    while i < len(xs):
        if xs[i] != ys[i]:
            return False
        i += 1
    return True


def max(xs: list[int]) -> int:
    """Determines largest number in a list."""
    if len(xs) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    top: int = xs[0]
    while i < len(xs):
        if xs[i] > top:
            top = xs[i]
        i += 1
    return top