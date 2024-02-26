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


Solution = SolutionSimple
