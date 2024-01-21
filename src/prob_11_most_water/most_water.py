from typing import List

# Complexity simple:
#   * Runtime: O(n^2)
#   * Space: O(1)
# Complexity best conceivable:
#   * Runtime: O(n)
#   * Space: O(1)


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        for i, h_i in enumerate(height):
            for j, h_j in enumerate(height):
                area = abs(i-j) * min(h_i, h_j)
                if area > max:
                    max = area

        return max
