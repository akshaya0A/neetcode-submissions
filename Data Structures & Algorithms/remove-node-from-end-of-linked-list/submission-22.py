class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        first = head
        second = head
        i = 0

        # move second n steps ahead
        while i < n:
            if not second:
                return head
            second = second.next
            i += 1

        # if removing the head
        if not second:
            return head.next

        # move both pointers
        while second.next:
            first = first.next
            second = second.next

        first.next = first.next.next
        return head
