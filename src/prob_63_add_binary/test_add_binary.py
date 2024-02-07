from .add_binary import Solution

solution = Solution()


def test_example1():
    assert solution.addBinary("11", "1") == "100"


def test_example2():
    assert solution.addBinary("1010", "1011") == "10101"
