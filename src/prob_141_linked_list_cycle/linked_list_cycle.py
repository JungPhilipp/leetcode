from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#   * Runtime: O(n): iterate once, constant look up in set
#   * Space: O(n): space for set
class SolutionHashSet:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        while head is not None and head.next is not None:
            if id(head) in nodes:
                return True
            nodes.add(id(head))
            head = head.next
        return False

#   * Runtime: O(n):
#   * Space: O(1): only two variables
class SolutionTwoPointers:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

Solution = SolutionTwoPointers
