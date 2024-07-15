class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while curr and curr.next:
            next_pair = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = next_pair
            prev.next = second

            prev = curr
            curr = next_pair

        return dummy.next
