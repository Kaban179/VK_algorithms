from importlib import import_module

import pytest

from Hometask_2.tests.list_node import make_list


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], None),
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 3], 2),
        ([1, 2, 3, 4], 3),
        ([5, 1, 9, 3, 8], 9),
        ([-2, -1], -1),
        ([0, 1, 2, 3, 4, 5], 3),
        ([4, 4, 4, 4, 4], 4),
        ([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 60),
    ],
)
def test_middle_node(values, expected):
    solution = import_module("Hometask_2.№2").Solution()
    result = solution.middleNode(make_list(values))
    assert (None if result is None else result.val) == expected
