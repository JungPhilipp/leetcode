from .first_occurrence import Solution

solution = Solution()


def test_example_1():
    assert solution.strStr("ssadbutsad", "sad") == 1


def test_example_2():
    assert solution.strStr("leetcode", "leeto") == -1

def test_example_3():
    assert solution.strStr("a", "a") == 0

def test_example_4():
    assert solution.strStr("aaa", "aaaa") == -1
