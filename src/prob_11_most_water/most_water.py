from typing import List

# Complexity simple:
#   * Runtime: O(n^2)
#   * Space: O(1)
# Complexity best conceivable:
#   * Runtime: O(n)
#   * Space: O(1)


class Solution:
    def area(self, height, i, j):
        return (j - i) * min(height[i], height[j])

    def maxArea(self, height: List[int]) -> int:
        front = 0
        back = len(height) - 1
        max_front = front
        max_back = back
        max = self.area(height, max_front, max_back)

        while front < back:
            if height[front] < height[max_front]:
                front += 1
                continue
            if height[back] < height[max_back]:
                back -= 1
                continue

            area = self.area(height, front, back)
            if area > max:
                max = area
                max_front = front
                max_back = back
            if height[front] < height[back]:
                front += 1
            else:
                back -= 1
        return max
