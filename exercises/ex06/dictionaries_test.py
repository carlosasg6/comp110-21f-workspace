"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests

from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730330989"


def test_invert_ex1() -> None:
    """Invert example given."""
    a: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(a) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_ex2() -> None:
    """Invert example 2 given."""
    a: dict[str, str] = {'apple': 'cat'}
    assert invert(a) == {'cat': 'apple'}


def test_invert_ex3() -> None:
    """Invert example 3 given."""
    a: dict[str, str] = {'ay': 'ya', 'yo': 'ho'}
    assert invert(a) == {'ya': 'ay', 'ho': 'yo'}


def test_favorite_color_ex1() -> None:
    """Test for use 1."""
    a: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(a) == "blue"


def test_favorite_color_ex2() -> None:
    """Test for use 2."""
    a: dict[str, str] = {"Carl": "green", "Pao": "blue", "Alexa": "black", "mom": "Purple", "dad": "blue"}
    assert favorite_color(a) == "blue"


def test_favorite_color_ex3() -> None:
    """Test for edge."""
    a: dict[str, str] = {"Marc": "yellow", "Kris": "blue"}
    assert favorite_color(a) == "yellow"


def test_count_ex1() -> None:
    """Test for count use 1."""
    a: list[str] = ["one", "one", "two"]
    assert count(a) == {'one': 2, 'two': 1}


def test_count_ex2() -> None:
    """Test for count use 2."""
    a: list[str] = ["one", "one", "one"]
    assert count(a) == {'one': 3}


def test_count_ex3() -> None:
    """Test for count edge."""
    a: list[str] = ["one"]
    assert count(a) == {'one': 1}