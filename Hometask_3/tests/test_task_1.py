from importlib import import_module

import pytest


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 2),
        (8, 2),
        (9, 3),
        (15, 3),
        (16, 4),
        (17, 4),
        (2147395599, 46339),
        (2147395600, 46340),
        (2147483647, 46340),
    ],
)
def test_integer_square_root(value, expected):
    solution = import_module("Hometask_3.№1").Solution()
    assert solution.mySqrt(value) == expected
