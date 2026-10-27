from importlib import import_module

import pytest


@pytest.mark.parametrize(
    ("numbers", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, True),
        ([2, 3, 4], 6, True),
        ([-1, 0], -1, True),
        ([0, 0, 3, 4], 0, True),
        ([-3, 3, 4, 90], 0, True),
        ([1, 2, 3, 4, 5], 8, True),
        ([1, 2, 3, 5], 6, True),
        ([5, 25, 75], 100, True),
        ([-10, -3, 0, 5, 11], 2, True),
        ([1, 3, 6, 9, 14], 20, True),
        ([], 0, False),
        ([1], 2, False),
        ([1, 2, 3], 10, False),
        ([-4, -2, 0], 3, False),
    ],
)
def test_two_sum_on_sorted_array(numbers, target, expected):
    solution = import_module("Hometask_2.№5").Solution()
    assert solution.twoSum(numbers, target) is expected
