from importlib import import_module
from math import comb

import pytest


Solution = import_module("Hometask_6.№2").Solution


@pytest.mark.parametrize("num_rows", range(1, 13))
def test_generate_pascal_triangle(num_rows):
    expected = [
        [comb(row, column) for column in range(row + 1)]
        for row in range(num_rows)
    ]
    assert Solution().generate(num_rows) == expected
