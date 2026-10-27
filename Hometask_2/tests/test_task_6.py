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
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        (".,", True),
        ("0P", False),
        ("No lemon, no melon", True),
    ],
)
def test_is_palindrome(text, expected):
    solution = import_module("Hometask_2.№6").Solution()
    assert solution.isPalindrome(text) is expected
