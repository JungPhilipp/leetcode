from typing import List

import sys

# Complexity simple:
#   * Runtime: O(n^2) Check all pairs
#   * Space: O(1)
# Complexity best conceivable:
#   * Runtime: O(n) look at every element only once
#   * Space: O(1) only two variables


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = sys.maxsize
        for price in prices:
            if price < min_price:
                min_price = price
                continue
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit
