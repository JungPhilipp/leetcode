from .best_time import Solution

solution = Solution()


def test_example1():
    assert solution.maxProfit([7,1,5,3,6,4]) == 5


def test_example2():
    assert solution.maxProfit([7,6,4,3,1]) == 0
