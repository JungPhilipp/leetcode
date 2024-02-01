from .climbing_stairs import Solution

solution = Solution()


def test_example1():
    assert solution.climbStairs(2) == 2


def test_example2():
    assert solution.climbStairs(3) == 3

def test_example3():
    assert solution.climbStairs(44) == 1134903170
