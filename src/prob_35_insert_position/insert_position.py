# Complexity simple:
#   * Runtime: O(n)
#   * Space: O(1)
# Complexity best conceivable:
#   * Runtime: O(log n) binary search
#   * Space: O(1)

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        interval = nums
        interval_start = 0
        while True:
            print(interval_start, interval)
            if len(interval) == 0:
                return interval_start
            if len(interval) == 1:
                return interval_start + int(target > interval[0])

            pivot_index = len(interval) // 2
            pivot = interval[pivot_index]

            if target == pivot:
                return interval_start + pivot_index
            if target < pivot:
                interval = interval[:pivot_index]
            else:
                interval_start += pivot_index
                interval = interval[pivot_index:]
