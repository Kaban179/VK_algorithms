from importlib import import_module


def test_remove_duplicates_in_place():
    solution = import_module("Hometask_2.№7").Solution()
    nums = [1, 1, 2]
    length = solution.removeDuplicates(nums)
    assert length == 2
    assert nums[:length] == [1, 2]
