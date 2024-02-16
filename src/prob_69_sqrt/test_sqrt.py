from .sqrt import Solution

solution = Solution()


def test_example1():
    assert solution.mySqrt(4) == 2


def test_example2():
    assert solution.mySqrt(8) == 2


def test_example3():
    assert solution.mySqrt(0) == 0


def test_example4():
    assert solution.mySqrt(1) == 1


def test_example5():
    assert solution.mySqrt(2) == 1


def test_example6():
    assert solution.mySqrt(6) == 2


def test_example7():
    assert solution.mySqrt(9) == 3


def test_example8():
    assert solution.mySqrt(2147395599) == 46339
