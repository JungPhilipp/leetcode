# Complexity simple:
#   * Runtime: O(log n):
#   * Space: O(log n): Stack space for recursion = depth of tree

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    last = None
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 2147483647
        diff = self.getMinimumDifference(root.left)
        if self.last and root.val - self.last.val < diff:
            diff = root.val - self.last.val
        self.last = root
        return min(diff, self.getMinimumDifference(root.right))
