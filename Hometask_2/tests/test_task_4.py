from importlib import import_module

import pytest


@pytest.mark.parametrize(
    ("source", "text", "expected"),
    [
        ("", "", True),
        ("", "abc", True),
        ("a", "", False),
        ("a", "a", True),
        ("a", "b", False),
        ("abc", "abc", True),
        ("ace", "abcde", True),
        ("aec", "abcde", False),
        ("aaa", "aa", False),
        ("bb", "ahbgdc", False),
        ("axc", "ahbgdc", False),
        ("ABC", "aBc", False),
    ],
)
def test_is_subsequence(source, text, expected):
    solution = import_module("Hometask_2.№4").Solution()
    assert solution.isSubsequence(source, text) is expected
