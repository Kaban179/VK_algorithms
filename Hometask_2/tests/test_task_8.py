from importlib import import_module

import pytest

from Hometask_2.tests.list_node import ListNode, list_values, make_list


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        ([], [], []),
        ([], [1], [1]),
        ([1], [], [1]),
        ([1], [2], [1, 2]),
        ([1, 3], [2, 4], [1, 2, 3, 4]),
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([-5, -1, 3], [-4, 0, 2], [-5, -4, -1, 0, 2, 3]),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5, 6]),
        ([2, 2, 2], [2, 2], [2, 2, 2, 2, 2]),
        ([1, 5, 9], [2, 3, 4, 10], [1, 2, 3, 4, 5, 9, 10]),
    ],
)
def test_merge_two_sorted_lists(first, second, expected):
    module = import_module("Hometask_2.№8")
    module.ListNode = ListNode
    solution = module.Solution()
    result = solution.mergeTwoLists(make_list(first), make_list(second))
    assert list_values(result) == expected


def test_merge_reuses_existing_nodes():
    module = import_module("Hometask_2.№8")
    module.ListNode = ListNode
    solution = module.Solution()
    first = make_list([1, 3])
    second = make_list([2, 4])
    original_nodes = []
    for head in (first, second):
        node = head
        while node is not None:
            original_nodes.append(node)
            node = node.next

    result = solution.mergeTwoLists(first, second)
    result_nodes = []
    node = result
    while node is not None:
        result_nodes.append(node)
        node = node.next

    assert sorted(map(id, result_nodes)) == sorted(map(id, original_nodes))
