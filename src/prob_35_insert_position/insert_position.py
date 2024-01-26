# Complexity simple:
#   * Runtime: O(n)
#   * Space: O(1)
# Complexity best conceivable:
#   * Runtime: O(log n) binary search
#   * Space: O(1)

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, element in enumerate(nums):
            if element < target:
                continue
            if element >= target:
                return index

        return len(nums)
