from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#   * Runtime: O(n): iterate through all nodes once
#   * Space: O(log n): stack space for recursion
class SolutionRecursive:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


#   * Runtime: O(n): iterate through all nodes once
#   * Space: O(log n): stack to keep track of nodes to be visited
class SolutionIterative:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        max = 0
        while len(stack) != 0:
            (next, depth) = stack.pop()
            if not next:
                if depth > max:
                    max = depth
                continue

            stack.append((next.left, depth + 1))
            stack.append((next.right, depth + 1))
        return max


Solution = SolutionIterative
