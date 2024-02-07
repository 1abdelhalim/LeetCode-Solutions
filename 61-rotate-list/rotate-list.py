# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head
        n = 1  
        
        while cur.next:
            cur = cur.next
            n += 1
        
        k = k % n
        if k == 0:
            return head
        
        for _ in range(n - k):
            prev = prev.next
        
        cur.next = head
        head = prev.next
        prev.next = None
        
        return head
