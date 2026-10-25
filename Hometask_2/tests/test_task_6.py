from importlib import import_module


def test_is_palindrome():
    solution = import_module("Hometask_2.№6").Solution()
    assert solution.isPalindrome("A man, a plan, a canal: Panama") is True
    assert solution.isPalindrome("race a car") is False
    assert solution.isPalindrome("") is True
