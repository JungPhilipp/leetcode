from .reverse_bits import Solution

solution = Solution()


def test_example1():
    assert solution.reverseBits(0b00000010100101000001111010011100) == 964176192


def test_example2():
    assert solution.reverseBits(0b11111111111111111111111111111101) == 3221225471

def test_example3():
    assert solution.reverseBits(0b00000000000000000000000000000001) == 2**31
