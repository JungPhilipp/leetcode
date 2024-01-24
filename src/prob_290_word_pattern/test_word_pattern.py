from .word_pattern import Solution

solution = Solution()


def test_example1():
    assert solution.wordPattern("abba", "dog cat cat dog") == True


def test_example2():
    assert solution.wordPattern("abba", "dog cat cat fish") == False


def test_example3():
    assert solution.wordPattern("aaaa", "dog cat cat dog") == False
