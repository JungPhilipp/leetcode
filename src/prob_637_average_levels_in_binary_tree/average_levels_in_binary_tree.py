# Complexity simple:
#   * Runtime: O(log n):
#   * Space: O(log n): Stack space for recursion and sum for each level, both log n

from collections import defaultdict
from typing import Optional, List, Tuple, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels: Dict[int, Tuple[int, int]] = defaultdict(lambda: (0,0))
        stack = [(root, 0)]
        while len(stack) > 0:
            (node, level) = stack.pop(0)
            if not node:
                continue
            sum, counter = levels[level]
            levels[level] = (sum + node.val, counter + 1)
            stack.extend([(node.left, level + 1), (node.right, level + 1)])

        return [sum / counter for (sum, counter) in levels.values()]
