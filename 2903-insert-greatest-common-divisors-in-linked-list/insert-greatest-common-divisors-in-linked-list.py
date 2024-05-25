# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val = val
#         self.next = next

import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            gcd_value = math.gcd(curr.val, curr.next.val)
            new_node = ListNode(gcd_value)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        
        return head
