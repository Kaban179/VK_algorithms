from importlib import import_module

import pytest


@pytest.mark.parametrize(
    ("animals", "portions", "expected"),
    [
        ([], [], 0),
        ([1], [], 0),
        ([1], [1], 1),
        ([2], [1], 0),
        ([2], [2], 1),
        ([1, 2, 3], [1, 1], 1),
        ([1, 2], [1, 2, 3], 2),
        ([1, 2, 3], [3], 1),
        ([2, 3], [1, 2, 3], 2),
        ([1, 1, 1], [1, 1], 2),
        ([4, 5, 6], [1, 2, 3], 0),
        ([2, 2, 3], [2, 2, 2], 2),
        ([1, 2, 2, 3], [1, 2, 2], 3),
        ([1, 2, 3], [3, 3, 3], 3),
        ([1, 2, 3], [1, 2, 3], 3),
    ],
)
def test_maximum_animals_fed(animals, portions, expected):
    solution = import_module("Hometask_3.№3").Solution()
    assert solution.findContentChildren(animals, portions) == expected
