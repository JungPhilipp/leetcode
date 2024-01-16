from .majority_element import Solution

solution = Solution()


def test_example1():
    assert solution.majorityElement([3, 2, 3]) == 3


def test_example2():
    assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
