from typing import Dict, List


# Complexity simple:
#   * Runtime: O(n) count occurrences of all values + O(m) find max
#   * Space: O(m) m, number of distinct values
# Complexity best conceivable:
#   * Runtime: O(n) look at every element only once
#   * Space: O(1)


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        values: Dict[int,int] = {}
        for element in nums:
            if element in values:
                values[element] += 1
            else:
                values[element] = 1
        return max(values, key=values.get)

