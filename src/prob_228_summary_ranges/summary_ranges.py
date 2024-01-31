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

    def summaryRanges(self, nums: List[int]) -> List[str]:
        intervals = []
        start = 0
        while start < len(nums):
            end = self.findEnd(start, nums)
            intervals.append([nums[start], nums[end]])
            start = end + 1

        return [
            f"{start}->{end}" if start != end else str(start)
            for start, end in intervals
        ]
