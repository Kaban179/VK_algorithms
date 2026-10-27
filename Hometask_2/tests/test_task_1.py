from importlib import import_module

import pytest

from Hometask_2.tests.list_node import ListNode, list_values, make_list


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [3, 2, 1]),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([-1, 0, 1], [1, 0, -1]),
        ([5, 5, 5], [5, 5, 5]),
        ([2, 1, 1], [1, 1, 2]),
        ([-7, -3], [-3, -7]),
        ([9, 8, 7, 6, 5], [5, 6, 7, 8, 9]),
    ],
)
def test_reverse_list(values, expected):
    solution = import_module("Hometask_2.№1").Solution()
    assert list_values(solution.reverseList(make_list(values))) == expected


def test_reverse_list_reuses_existing_nodes():
    solution = import_module("Hometask_2.№1").Solution()
    head = make_list([1, 2, 3])
    original_nodes = []
    node = head
    while node is not None:
        original_nodes.append(node)
        node = node.next

    result = solution.reverseList(head)
    result_nodes = []
    node = result
    while node is not None:
        result_nodes.append(node)
        node = node.next

    assert result_nodes == original_nodes[::-1]
