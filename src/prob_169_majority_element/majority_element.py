from typing import List


# Complexity simple:
#   * Runtime: O(n) count occurrences of all values + O(m) find max
#   * Space: O(m) m, number of distinct values
# Complexity best conceivable: (Boyer Moore Voting)
#   * Runtime: O(n) look at every element only once
#   * Space: O(1) only two variables


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        frequency = 0
        for num in nums:
            if frequency == 0:
                majority = num
            if num == majority:
                frequency += 1
            else:
                frequency -= 1

        return majority
