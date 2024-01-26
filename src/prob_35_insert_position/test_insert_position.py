from .insert_position import Solution

solution = Solution()


def test_example1():
    assert solution.searchInsert([1, 3, 5, 6], 5) == 2


def test_example2():
    assert solution.searchInsert([1, 3, 5, 6], 2) == 1


def test_example3():
    assert solution.searchInsert([1, 3, 5, 6], 7) == 4
