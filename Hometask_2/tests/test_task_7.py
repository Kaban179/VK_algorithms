from importlib import import_module

import pytest


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([1, 1], [1]),
        ([1, 2], [1, 2]),
        ([1, 1, 2], [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
        ([-3, -3, -1, 0, 0], [-3, -1, 0]),
        ([1, 1, 1, 1], [1]),
        ([-5, -2, 0, 3, 9], [-5, -2, 0, 3, 9]),
        ([1, 2, 2, 3, 4, 4, 5, 5, 6], [1, 2, 3, 4, 5, 6]),
    ],
)
def test_remove_duplicates_in_place(values, expected):
    solution = import_module("Hometask_2.№7").Solution()
    nums = values.copy()
    length = solution.removeDuplicates(nums)
    assert length == len(expected)
    assert nums[:length] == expected
