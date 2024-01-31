# Complexity simple:
#   * Runtime: O(n):
#   * Space: O(n): return
# Complexity best conceivable:
#   * Runtime: O(n):
#   * Space: O(n)


from typing import List, Optional


class Solution:
    def findEnd(self, first: int, nums: List[int]) -> Optional[int]:
        if first >= len(nums):
            return None
        last_element = nums[first]
        next = first + 1
        while next < len(nums) and nums[next] == last_element + 1:
            last_element = nums[next]
            next += 1
        return next - 1

    def interval(self, start: int, end: int, nums: List[int]) -> str:
        if start == end:
            return str(nums[start])
        return f"{nums[start]}->{nums[end]}"

    def summaryRanges(self, nums: List[int]) -> List[str]:
        intervals = []
        start = 0
        while start < len(nums):
            end = self.findEnd(start, nums)
            intervals.append(self.interval(start, end, nums))
            start = end + 1

        return intervals
