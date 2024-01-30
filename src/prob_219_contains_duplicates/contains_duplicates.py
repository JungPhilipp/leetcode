# Complexity simple:
#   * Runtime: O(n * k):
#   * Space: O(1)
# Complexity best conceivable:
#   * Runtime: O(n):
#   * Space: O(1)


from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        interval = set(nums[:k])
        if len(interval) < min(k, len(nums)):
            return True

        for i, current in enumerate(nums):
            j = i + k
            if j >= len(nums):
                break;
            next = nums[j]
            if next in interval:
                return True
            interval.remove(current)
            interval.add(next)


        return False
