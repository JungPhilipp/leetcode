from .plus_one import Solution

solution = Solution()


def test_example1():
    assert solution.plusOne([1,2,3]) == [1,2,4]


def test_example2():
    assert solution.plusOne([4,3,2,1]) == [4,3,2,2]

def test_example3():
    assert solution.plusOne([9]) == [1,0]
