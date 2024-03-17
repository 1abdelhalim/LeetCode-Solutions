# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next

        curr = head

        for i in range(len(stack) // 2):
            next_node = curr.next
            curr.next = stack.pop()
            curr.next.next = next_node
            curr = next_node

        if curr:
            curr.next = None

        