from importlib import import_module


def test_is_subsequence():
    solution = import_module("Hometask_2.№4").Solution()
    assert solution.isSubsequence("ace", "abcde") is True
    assert solution.isSubsequence("aec", "abcde") is False
    assert solution.isSubsequence("", "abcde") is True
