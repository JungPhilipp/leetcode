from typing import List, Optional

#   * Runtime: O(1):
#   * Space: O(1):


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        pivot_index = len(nums) // 2
        return TreeNode(
            val=nums[pivot_index],
            left=self.sortedArrayToBST(nums[:pivot_index]),
            right=self.sortedArrayToBST(nums[pivot_index + 1:]),
        )
