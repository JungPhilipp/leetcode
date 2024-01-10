from .merge_sorted import Solution

solution = Solution()

def test_example_1():
    nums1 = [1,2,3,0,0,0]
    solution.merge(nums1, 3, [2,5,6], 3)
    assert nums1 == [1,2,2,3,5,6]
