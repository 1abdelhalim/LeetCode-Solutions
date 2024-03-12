class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l = headA
        r = headB

        while l != r :
            l = headB if l is None else l.next
            r = headA if r is None else r.next
        return l