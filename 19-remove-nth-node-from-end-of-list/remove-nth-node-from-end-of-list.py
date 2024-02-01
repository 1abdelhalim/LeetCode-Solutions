# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        l, r = dummy, dummy

        for _ in range(n + 1):
            r = r.next

        while r:
            l = l.next
            r = r.next
        l.next = l.next.next

        return dummy.next