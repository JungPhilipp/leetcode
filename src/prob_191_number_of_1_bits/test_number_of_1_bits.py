from .number_of_1_bits import Solution

solution = Solution()


def test_example1():
    assert solution.hammingWeight(0b00000000000000000000000000001011) == 3


def test_example2():
    assert solution.hammingWeight(0b00000000000000000000000010000000) == 1


def test_example3():
    assert solution.hammingWeight(0b11111111111111111111111111111101) == 31
