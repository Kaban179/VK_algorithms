from importlib import import_module

from Hometask_2.tests.list_node import list_values, make_list


def test_remove_elements():
    solution = import_module("Hometask_2.№3").Solution()
    result = solution.removeElements(make_list([1, 2, 6, 3, 6]), 6)
    assert list_values(result) == [1, 2, 3]


def test_remove_all_elements():
    solution = import_module("Hometask_2.№3").Solution()
    result = solution.removeElements(make_list([7, 7]), 7)
    assert result is None
