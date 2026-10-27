from importlib import import_module

import pytest


@pytest.mark.parametrize(
    ("numbers", "target", "expected"),
    [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([0, 0, 3, 4], 0, [1, 2]),
        ([-3, 3, 4, 90], 0, [1, 2]),
        ([1, 2, 3, 4, 5], 8, [3, 5]),
        ([1, 2, 3, 5], 6, [1, 4]),
        ([5, 25, 75], 100, [2, 3]),
        ([-10, -3, 0, 5, 11], 2, [2, 4]),
        ([1, 3, 6, 9, 14], 20, [3, 5]),
    ],
)
def test_two_sum_on_sorted_array(numbers, target, expected):
    solution = import_module("Hometask_2.№5").Solution()
    assert solution.twoSum(numbers, target) == expected
