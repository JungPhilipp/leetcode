from .ransom import Solution

solution = Solution()


def test_example1():
    assert solution.canConstruct("a", "b") == False


def test_example2():
    assert solution.canConstruct("aa", "ab") == False


def test_example3():
    assert solution.canConstruct("aa", "aab") == True

def test_example4():
    assert solution.canConstruct("aaa", "aab") == False
