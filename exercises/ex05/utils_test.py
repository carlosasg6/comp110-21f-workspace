"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "730330989"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_none() -> None:
    xs: list[int] = [1, 5, 3]
    assert only_evens(xs) == []


def test_only_evens_all() -> None:
    xs: list[int] = [4, 2, 4, 4]
    assert only_evens(xs) == [4, 2, 4, 4]


def test_only_evens_some() -> None:
    xs: list[int] = [1, 2, 3, 4]
    assert only_evens(xs) == [2, 4]


def test_sub_use() -> None:
    xs: list[int] = [1, 2, 3, 4, 5, 6]
    start: int = 1
    end: int = 5
    assert sub(xs, start, end) == [2, 3, 4, 5]


def test_sub_use_ex() -> None:
    xs: list[int] = [10, 20, 30, 40]
    start: int = 1
    end: int = 3
    assert sub(xs, start, end) == [20, 30]


def test_sub_neg_start_long_end() -> None:
    xs: list[int] = [1, 2, 3, 4]
    start: int = -1
    end: int = 6
    assert sub(xs, start, end) == [1, 2, 3]


def test_concat_nothin() -> None:
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_lotta() -> None:
    xs: list[int] = [1, 2, 3, 4]
    ys: list[int] = [5, 6, 7, 8]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6, 7, 8]


def test_concat_negs() -> None:
    xs: list[int] = [-1, -2, -3]
    ys: list[int] = [10, -30, 20]
    assert concat(xs, ys) == [-1, -2, -3, 10, -30, 20]