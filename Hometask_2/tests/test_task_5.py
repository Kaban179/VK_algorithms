from importlib import import_module


def test_two_sum_on_sorted_array():
    solution = import_module("Hometask_2.№5").Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [1, 2]
