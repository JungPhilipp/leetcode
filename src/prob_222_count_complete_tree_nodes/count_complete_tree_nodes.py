from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#   * Runtime: O(n): visit all nodes
#   * Space: O(log n): stack space for recursion


class SolutionSimple:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        queue = [root]
        while queue:
            node = queue.pop()
            if not node:
                continue
            count += 1
            queue.append(node.left)
            queue.append(node.right)
        return count


#   * Runtime: O(log n * log n): binary search (log n) * traverse to lowest level (log n)
#   * Space: O(log n): stack space for recursion


class SolutionLinear:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        depthLeft = self.depthLeft(root)
        depthRight = self.depthRight(root)
        maxCount = pow(2, depthLeft) - 1

        if depthLeft == depthRight:
            return maxCount

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def depthLeft(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + self.depthLeft(node.left)

    def depthRight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        return 1 + self.depthRight(node.right)


Solution = SolutionLinear
