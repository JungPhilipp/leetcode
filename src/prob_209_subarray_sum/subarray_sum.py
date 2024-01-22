from math import log
import sys
from typing import List, Optional

# Complexity simple:
#   * Runtime: O(n *m) n = len(nums) and m = target
#   * Space: O(1)
# Complexity best conceivable:
#   * Runtime: O(n)
#   * Space: O(1)


class Solution:
    def binarySearch(self, target: int, nums: List[int]) -> Optional[int]:
        i = len(nums)
        while i >= 0 and i <= len(nums):
            print(len(nums), i)
            count = sum(nums[:i])
            if count < target and i < len(nums) and count + nums[i] >= target:
                return i
            if count < target:
                i += max(1, (len(nums) - i) // 2)
            else:
                i -= max(1, i // 2)

        return None

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min = sys.maxsize
        for start in range(len(nums)):
            end = self.binarySearch(target, nums[start:])
            print(end)
            if end == None:
                continue
            if end < min:
                min = end

        return min + 1 if min != sys.maxsize else 0
