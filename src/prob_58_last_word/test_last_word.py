from .last_word import Solution

solution = Solution()


def test_example_1():
    assert solution.lengthOfLastWord("Hello World") == 5


def test_example_2():
    assert solution.lengthOfLastWord("   fly me   to   the moon  ") == 4


def test_example_3():
    assert solution.lengthOfLastWord("luffy is still joyboy") == 6
