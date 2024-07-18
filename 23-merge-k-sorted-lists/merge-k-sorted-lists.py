# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = []
        for l in lists:
            curr = l 
            while curr:
                result.append(curr.val)
                curr = curr.next

        result.sort()
        n = len(result)

        if n == 0:
            return None 
        
        head = ListNode(result[0])
        start = head
        for i in range(1, n):
            head.next = ListNode(result[i])
            head = head.next 

        return start 