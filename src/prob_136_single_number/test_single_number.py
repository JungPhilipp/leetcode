from .single_number import Solution

solution = Solution()


def test_example1():
    assert solution.singleNumber([2, 2, 1]) == 1


def test_example2():
    assert solution.singleNumber([4, 1, 2, 1, 2]) == 4


def test_example3():
    assert solution.singleNumber([1]) == 1
