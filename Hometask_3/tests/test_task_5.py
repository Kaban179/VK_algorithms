from importlib import import_module

import pytest


@pytest.mark.parametrize(
    ("nums", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([0, 4, 3, 0], 0, [0, 3]),
        ([-3, 4, 3, 90], 0, [0, 2]),
        ([-10, -3, 0, 5, 11], 2, [1, 3]),
        ([1, 2, 5, 8], 10, [1, 3]),
        ([1, 4, 5, 11], 9, [1, 2]),
        ([1, 2, 3], 7, []),
        ([1, 1, 1], 3, []),
        ([5, 6], 10, []),
        ([0, -1, 2], 2, [0, 2]),
        ([8, 1, 4, 2], 9, [0, 1]),
        ([5, 75, 25], 100, [1, 2]),
    ],
)
def test_two_sum(nums, target, expected):
    solution = import_module("Hometask_3.№5").Solution()
    assert solution.twoSum(nums, target) == expected
