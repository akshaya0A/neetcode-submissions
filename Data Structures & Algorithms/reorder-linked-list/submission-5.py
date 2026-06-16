class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        slow = head
        fast = head

        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split
        mid = slow.next
        slow.next = None

        # reverse second half
        prev = None
        while mid:
            nxt = mid.next
            mid.next = prev
            prev = mid
            mid = nxt

        # merge
        curr2 = head
        curr3 = prev

        while curr3:
            temp1 = curr2.next
            temp2 = curr3.next

            curr2.next = curr3
            curr3.next = temp1

            curr2 = temp1
            curr3 = temp2
