from importlib import import_module

import pytest


@pytest.mark.parametrize(
    ("original", "shuffled", "extra"),
    [
        ("", "a", "a"),
        ("a", "aa", "a"),
        ("abcd", "abcde", "e"),
        ("aabc", "abacd", "d"),
        ("xyz", "xyzz", "z"),
        ("zzzz", "zzzzx", "x"),
        ("aabbcc", "abcbaca", "a"),
        ("mnop", "pmnqo", "q"),
        ("aaa", "aaaa", "a"),
        ("ab", "bca", "c"),
        ("c", "dc", "d"),
        ("a", "ba", "b"),
        ("abc", "cabd", "d"),
        ("aabb", "babac", "c"),
    ],
)
def test_find_added_character(original, shuffled, extra):
    solution = import_module("Hometask_3.№4").Solution()
    assert solution.findTheDifference(original, shuffled) == extra
