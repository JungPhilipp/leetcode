from .valid_palindrome import Solution

solution = Solution()


def test_example1():
    assert solution.isPalindrome("A man, a plan, a canal: Panama") == True


def test_example2():
    assert solution.isPalindrome("race a car") == False


def test_example3():
    assert solution.isPalindrome(" ") == True
