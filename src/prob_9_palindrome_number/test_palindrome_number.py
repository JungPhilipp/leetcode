from .palindrome_number import Solution

solution = Solution()


def test_single_digit():
    assert solution.isPalindrome(0) is True
    assert solution.isPalindrome(1) is True
    assert solution.isPalindrome(5) is True
    assert solution.isPalindrome(9) is True


def test_example_1():
    assert solution.isPalindrome(121) is True


def test_example_2():
    assert solution.isPalindrome(123) is False


def test_example_3():
    assert solution.isPalindrome(10) is False


def test_even_number_of_digits():
    assert solution.isPalindrome(5050) is False
    assert solution.isPalindrome(5665) is True
    assert solution.isPalindrome(2233) is False


def test_odd_number_of_digits():
    assert solution.isPalindrome(1331) is True
    assert solution.isPalindrome(13431) is True
    assert solution.isPalindrome(12222) is False


def test_negative_numbers():
    assert solution.isPalindrome(-1331) is False
    assert solution.isPalindrome(-1) is False
    assert solution.isPalindrome(-0) is True
    assert solution.isPalindrome(-5665) is False
