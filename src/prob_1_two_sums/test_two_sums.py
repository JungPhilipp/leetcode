from .two_sums import Solution

solution = Solution()


def test_empty():
    assert solution.twoSum([], 10) == []


def test_example1():
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_example2():
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]


def test_example3():
    assert solution.twoSum([3, 3], 6) == [0, 1]


def test_do_no_reuse_element():
    assert solution.twoSum([3], 6) == []


def test_negativ_numbers():
    assert solution.twoSum([-3, -2, -1, 0, -40], -4) == [0, 2]


def test_negativ_positive_numbers_mixed():
    assert solution.twoSum([-3, 2, -2, 0, 40], 0) == [1, 2]
