from typing import List


class Solution:
    def twoSumSimple(self, numbers: List[int], target: int) -> List[int]:
        for first_index, first in enumerate(numbers):
            for second_index, second in enumerate(numbers):
                if first_index == second_index:
                    continue
                if first + second == target:
                    return [first_index, second_index]
        return []

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        compliments = {}
        for first_index, first in enumerate(numbers):
            second_index = compliments.get(first)
            if second_index is None:
                compliments[target - first] = first_index
            else:
                return [second_index, first_index]
        return []


# Improved Solutions:
#    1. Overall O(n log n) Runtime and O(n) Memory if array cannot be sorted in place:
#       Sort array O(n log n) + iterate from front and back O(n),
#       move front when sum is too small, move back when sum is too large
#   2. Overall O(2n) = O(n)
#       Insert into Hashmap O(n): number -> key, index -> value
#       Iterate numbers and try lookup of numbers[i] - target O(n)
