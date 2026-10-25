from importlib import import_module

from Hometask_2.tests.list_node import list_values, make_list


def test_reverse_list():
    solution = import_module("Hometask_2.№1").Solution()
    assert list_values(solution.reverseList(make_list([1, 2, 3, 4]))) == [4, 3, 2, 1]
