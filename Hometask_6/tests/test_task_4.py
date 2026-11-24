from importlib import import_module

import pytest


Solution = import_module("Hometask_6.№4").Solution


def longest_palindrome_length(text):
    best = 0
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            candidate = text[start:end]
            if candidate == candidate[::-1]:
                best = max(best, len(candidate))
    return best


@pytest.mark.parametrize("text", [
    "a",
    "aa",
    "ab",
    "babad",
    "cbbd",
    "aaaa",
    "racecar",
    "abacdfgdcaba",
    "forgeeksskeegfor",
    "aacabdkacaa",
    "abcddcbaXYZ",
    "bananas",
    "noonabbad",
    "acbbca",
])
def test_longest_palindrome(text):
    result = Solution().longestPalindrome(text)
    assert result == result[::-1]
    assert result in text
    assert len(result) == longest_palindrome_length(text)
