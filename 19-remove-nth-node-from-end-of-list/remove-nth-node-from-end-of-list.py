# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr, prev = head, head
        for _ in range(n):
            curr = curr.next
        if not curr:
            return head.next
        while curr.next:
            curr, prev = curr.next, prev.next
        prev.next = prev.next.next
        return head
