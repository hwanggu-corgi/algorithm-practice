#  Reverse Linked List
#
# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
# =============== solution (recursion) ================
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if head == None or head.next == None:
            return head

        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return node


# =============== solution (iterative) ================

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        prev = None

        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next


        return prev