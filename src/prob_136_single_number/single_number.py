from typing import List
from functools import reduce


#   * Runtime: O(n): iterate once, constant look up in set
#   * Space: O(n): space for set
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda a, b: a ^ b, nums)
