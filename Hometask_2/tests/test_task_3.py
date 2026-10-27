from importlib import import_module

import pytest

from Hometask_2.tests.list_node import list_values, make_list


@pytest.mark.parametrize(
    ("values", "target", "expected"),
    [
        ([], 1, []),
        ([1], 1, []),
        ([1], 2, [1]),
        ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),
        ([7, 7], 7, []),
        ([1, 2, 3], 1, [2, 3]),
        ([1, 2, 3], 3, [1, 2]),
        ([1, 2, 3], 2, [1, 3]),
        ([2, 2, 2], 1, [2, 2, 2]),
        ([-1, 0, -1, 2], -1, [0, 2]),
    ],
)
def test_remove_elements(values, target, expected):
    solution = import_module("Hometask_2.№3").Solution()
    result = solution.removeElements(make_list(values), target)
    assert list_values(result) == expected
