from .valid_parentheses import Solution

solution = Solution()


def test_example_1():
    assert solution.isValid("()") is True


def test_example_2():
    assert solution.isValid("()[]{}") is True


def test_example_3():
    assert solution.isValid("(]") is False


def test_example_4():
    assert solution.isValid("(){}}{") is False
