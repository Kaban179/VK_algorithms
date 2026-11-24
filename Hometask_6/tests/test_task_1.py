from importlib import import_module
import pytest


Solution = import_module("Hometask_6.№1").Solution


@pytest.mark.parametrize(("nums", "expected"), [
    ([7], 1),
    ([1, 2, 3], 3),
    ([3, 2, 1], 1),
    ([5, 5, 5], 1),
    ([1, 3, 2, 4, 5], 3),
    ([3, 2, 8, 9, 5, 10], 3),
    ([1, 2, 7, 9, 0, 10], 4),
    ([-5, -4, -3, -8, -7], 3),
    ([1, 2, 3, 0], 3),
    ([0, 1, 2, 3], 4),
    ([1, 2, 2, 3, 4], 3),
    ([10, 1, 2, 3, 4, 5, 0, 1], 5),
])
def test_find_length_of_lcis(nums, expected):
    assert Solution().findLengthOfLCIS(nums) == expected
