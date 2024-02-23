# Complexity simple:
#   * Runtime: O(log n):
#   * Space: O(log n): space for avg

from collections import defaultdict, deque
from typing import Optional, List, Tuple, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        avgs = []
        queue = deque()
        queue.append(root)
        while queue:
            sum = 0.
            count = len(queue)
            for _ in range(count):
                node = queue.popleft()
                sum += node.val
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            avgs.append(sum / count)
        return avgs

