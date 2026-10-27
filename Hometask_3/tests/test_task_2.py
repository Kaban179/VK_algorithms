from importlib import import_module

import pytest


@pytest.mark.parametrize(
    ("copies", "first_time", "second_time", "expected"),
    [
        (1, 3, 5, 3),
        (2, 2, 3, 4),
        (3, 2, 3, 5),
        (4, 2, 3, 6),
        (5, 2, 3, 8),
        (6, 2, 3, 8),
        (4, 1, 5, 4),
        (5, 1, 2, 4),
        (10, 3, 4, 19),
        (10, 7, 10, 47),
        (100, 1, 1, 51),
        (4, 1, 1, 3),
        (5, 4, 4, 12),
        (10, 1, 2, 7),
    ],
)
def test_minimum_copy_time(copies, first_time, second_time, expected):
    solution = import_module("Hometask_3.№2").Solution()
    assert solution.minimumTime(copies, first_time, second_time) == expected
