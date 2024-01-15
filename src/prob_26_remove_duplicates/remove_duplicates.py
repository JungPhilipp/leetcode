from typing import List, Optional

# Complexity simple:
#   * Runtime: O(n) copy one of each to new array
#   * Space: O(n) new array possibly as large as input
# Complexity best conceivable:
#   * Runtime: O(n) look at every element only once
#   * Space: In-place O(0), no additional memory


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        index_search_start = index
        last_element = None
        count = len(nums)
        while index < count:
            index_next_element = self.posNextLargerElement(
                nums[index_search_start:], last_element
            )
            if index_next_element == None:
                return index
            index_next_element += index_search_start
            next_element = nums[index_next_element]
            nums[index] = next_element
            index += 1
            last_element = next_element
            index_search_start = index_next_element

        return index

    def posNextLargerElement(
        self, nums: List[int], element: Optional[int]
    ) -> Optional[int]:
        index = 0
        while index < len(nums):
            if element == None or nums[index] > element:
                return index
            index += 1
        return None
