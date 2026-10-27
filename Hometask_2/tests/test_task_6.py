from importlib import import_module

import pytest


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", True),
        ("a", True),
        ("aa", True),
        ("ab", False),
        ("aba", True),
        ("abba", True),
        ("abc", False),
        ("A man, a plan, a canal: Panama", False),
        ("race a car", False),
        (" ", True),
        (".,", False),
        ("No lemon, no melon", False),
        ("1221", True),
        ("1231", False),
        ("été", True),
        ("котток", True),
    ],
)
def test_is_palindrome(text, expected):
    solution = import_module("Hometask_2.№6").Solution()
    assert solution.isPalindrome(text) is expected
