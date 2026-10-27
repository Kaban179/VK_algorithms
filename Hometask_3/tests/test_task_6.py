from importlib import import_module

import pytest


def normalize(groups):
    return sorted(tuple(sorted(group)) for group in groups)


@pytest.mark.parametrize(
    ("words", "expected"),
    [
        ([], []),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["a", "b"], [["a"], ["b"]]),
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        ),
        (["ab", "ba", "abc", "cba", "a"], [["ab", "ba"], ["abc", "cba"], ["a"]]),
        (
            ["listen", "silent", "enlist", "google", "gooegl"],
            [["listen", "silent", "enlist"], ["google", "gooegl"]],
        ),
        (["same", "same"], [["same", "same"]]),
        (["", ""], [["", ""]]),
        (
            ["aab", "aba", "baa", "abb", "bab", "bba"],
            [["aab", "aba", "baa"], ["abb", "bab", "bba"]],
        ),
        (["rat", "tar", "art", "car"], [["rat", "tar", "art"], ["car"]]),
        (["", "b", ""], [["", ""], ["b"]]),
        (["abc", "bca", "cab", "xyz", "zyx", "xzy"], [["abc", "bca", "cab"], ["xyz", "zyx", "xzy"]]),
        (["a", "ab", "ba", "a"], [["a", "a"], ["ab", "ba"]]),
    ],
)
def test_group_anagrams(words, expected):
    solution = import_module("Hometask_3.№6").Solution()
    result = solution.groupAnagrams(words)
    assert normalize(result) == normalize(expected)
