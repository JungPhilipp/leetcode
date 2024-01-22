from .subarray_sum import Solution

solution = Solution()


def test_example1():
    assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2


def test_example2():
    assert solution.minSubArrayLen(4, [1, 4, 4]) == 1


def test_example3():
    assert solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0


def test_example3():
    assert solution.minSubArrayLen(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]) == 0
