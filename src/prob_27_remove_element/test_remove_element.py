from .remove_element import Solution

solution = Solution()


def test_example1():
    nums = [3, 2, 2, 3]
    assert solution.removeElement(nums, 3) == 2
    assert nums == [2, 2, 3, 3]


def test_example2():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    assert solution.removeElement(nums, 2) == 5
    assert nums == [0, 1, 4, 0, 3, 2, 2, 2]


def test_example3():
    nums = [4, 5]
    assert solution.removeElement(nums, 4) == 1
    assert nums == [5, 4]

def test_example3():
    nums = [1]
    assert solution.removeElement(nums, 1) == 0
    assert nums == [1]

def test_example3():
    nums = [3,3]
    assert solution.removeElement(nums, 5) == 2
    assert nums == [3,3]
