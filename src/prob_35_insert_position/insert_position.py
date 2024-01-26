# Complexity simple:
#   * Runtime: O(n)
#   * Space: O(1)
# Complexity best conceivable:
#   * Runtime: O(log n) binary search
#   * Space: O(1)

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if (len(nums)) == 0:
            return 0
        if len(nums) == 1:
            return int(target > nums[0])

        pivot_index = len(nums) // 2
        pivot = nums[pivot_index]

        if target == pivot:
            return pivot_index
        if target < pivot:
            return self.searchInsert(nums[:pivot_index], target)
        else:
            return pivot_index + self.searchInsert(nums[pivot_index:], target)
