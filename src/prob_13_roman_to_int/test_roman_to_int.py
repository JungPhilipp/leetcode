from .roman_to_int import Solution

solution = Solution()

def test_example_1():
    assert solution.romanToInt("III") == 3

def test_example_2():
    assert solution.romanToInt("LVIII") == 58

def test_example_3():
    assert solution.romanToInt("MCMXCIV") == 1994
