from importlib import import_module

from Hometask_2.tests.list_node import list_values, make_list


def test_merge_two_sorted_lists():
    solution = import_module("Hometask_2.№8").Solution()
    result = solution.mergeTwoLists(make_list([3, 6, 8]), make_list([4, 7, 9, 11]))
    assert list_values(result) == [3, 4, 6, 7, 8, 9, 11]
