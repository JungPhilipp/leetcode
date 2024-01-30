from .contains_duplicates import Solution

solution = Solution()


def test_example1():
    assert solution.containsNearbyDuplicate([1, 2, 3, 1], 3) == True


def test_example2():
    assert solution.containsNearbyDuplicate([1, 0, 1, 1], 1) == True


def test_example3():
    assert solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False


def test_example4():
    assert solution.containsNearbyDuplicate([1, 2, 1], 0) == False
