from .first_occurrence import Solution

solution = Solution()


def test_example_1():
    assert solution.strStr("sadbutsad", "sad") == 0


def test_example_2():
    assert solution.strStr("leetcode", "leeto") == -1
