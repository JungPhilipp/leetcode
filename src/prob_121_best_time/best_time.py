from typing import List

# Complexity simple:
#   * Runtime: O(n^2) Check all pairs
#   * Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for (index, buy_price) in enumerate(prices):
            for sell_price in prices[index:]:
                profit = sell_price - buy_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit
