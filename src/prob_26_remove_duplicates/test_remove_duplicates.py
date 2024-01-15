from .remove_duplicates import Solution

solution = Solution()


def test_example1():
    nums = [1, 1, 2]
    assert solution.removeDuplicates(nums) == 2
    assert nums[0:2] == [1, 2]


def test_example2():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert solution.removeDuplicates(nums) == 5
    assert nums[0:5] == [0, 1, 2, 3, 4]


def test_example3():
    nums = [0, 1, 2, 2, 2, 3]
    assert solution.removeDuplicates(nums) == 4
    assert nums[0:4] == [0, 1, 2, 3]

def test_example4():
    nums = []
    assert solution.removeDuplicates(nums) == 0
    assert nums == []
