from .happy_number import Solution

solution = Solution()


def test_example1():
    assert solution.isHappy(19) == True


def test_example2():
    assert solution.isHappy(2) == False
