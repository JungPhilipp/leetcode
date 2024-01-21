from .most_water import Solution

solution = Solution()


def test_example1():
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_example2():
    assert solution.maxArea([1, 1]) == 1

def test_example3():
    assert solution.maxArea([2,3,4,5,18,17,6]) == 17
