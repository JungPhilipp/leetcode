from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 0:
            return []
        for first_index, first in enumerate(numbers):
            for second_index, second in enumerate(numbers):
                if first_index == second_index:
                    continue
                if first + second == target:
                    return [first_index, second_index]
        return []
