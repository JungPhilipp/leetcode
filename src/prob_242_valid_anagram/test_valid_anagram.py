from .valid_anagram import Solution

solution = Solution()


def test_example1():
    assert solution.isAnagram("anagram", "nagaram") == True


def test_example2():
    assert solution.isAnagram("rat", "car") == False
