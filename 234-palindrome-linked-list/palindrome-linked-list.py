class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverseList(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev

 
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half_reversed = reverseList(slow)

        while second_half_reversed:
            if head.val != second_half_reversed.val:
                return False
            head = head.next
            second_half_reversed = second_half_reversed.next

        return True
