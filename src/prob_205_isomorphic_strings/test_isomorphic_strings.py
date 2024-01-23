from .isomorphic_strings import Solution

solution = Solution()


def test_example1():
    assert solution.isIsomorphic("egg", "add") == True


def test_example2():
    assert solution.isIsomorphic("foo", "bar") == False


def test_example3():
    assert solution.isIsomorphic("paper", "title") == True


def test_example4():
    assert solution.isIsomorphic("", "") == True


def test_example5():
    assert solution.isIsomorphic("", " ") == False


def test_example6():
    assert solution.isIsomorphic("badc", "baba") == False
