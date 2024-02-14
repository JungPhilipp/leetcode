from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#   * Runtime: O(n): visit all nodes
#   * Space: O(log n): stack space for recursion
class Solution:
    def areMirrored(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        return self.areMirrored(left.left, right.right) and self.areMirrored(
            left.right, right.left
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.areMirrored(root.left, root.right)
