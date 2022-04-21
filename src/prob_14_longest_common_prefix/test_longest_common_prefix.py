from .longest_common_prefix import Solution

solution = Solution()


def test_empty():
    assert solution.longestCommonPrefix([]) == ""


def test_example_1():
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"


def test_example_2():
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
