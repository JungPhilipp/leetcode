from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#   * Runtime: O(n): iterate through all nodes once
#   * Space: O(log n): stack space for recursion
class Solution:
    def invertNode(self, node: Optional[TreeNode]):
        if not node:
            return
        node.left, node.right = node.right, node.left
        self.invertNode(node.left)
        self.invertNode(node.right)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertNode(root)
        return root
