from importlib import import_module

from Hometask_2.tests.list_node import make_list


def test_middle_node_returns_middle():
    solution = import_module("Hometask_2.№2").Solution()
    assert solution.middleNode(make_list([1, 2, 3])).val == 2


def test_middle_node_returns_second_middle_for_even_length():
    solution = import_module("Hometask_2.№2").Solution()
    assert solution.middleNode(make_list([1, 2, 3, 4])).val == 3
