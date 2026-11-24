from importlib import import_module

import pytest


Solution = import_module("Hometask_6.№3").Solution


@pytest.mark.parametrize(("coins", "amount", "expected"), [
    ([1], 0, 0),
    ([1], 2, 2),
    ([2], 3, -1),
    ([1, 2, 5], 11, 3),
    ([2, 3, 5], 11, 3),
    ([2, 4], 7, -1),
    ([1], 10, 10),
    ([3, 7], 17, 3),
    ([10, 5, 2, 1], 27, 4),
    ([4, 6], 5, -1),
    ([4, 6], 8, 2),
    ([2, 5], 9, 3),
    ([7], 28, 4),
    ([1, 3, 4], 6, 2),
])
def test_coin_change(coins, amount, expected):
    assert Solution().coinChange(coins, amount) == expected
