from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#   * Runtime: O(m+n): iterate both list once
#   * Space: O(1):
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head = ListNode(0)
        beforeStart = head
        while list1 and list2:
            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next

            head = head.next

        while list1:
            head.next = list1
            list1 = list1.next
            head = head.next

        while list2:
            head.next = list2
            list2 = list2.next
            head = head.next

        return beforeStart.next
