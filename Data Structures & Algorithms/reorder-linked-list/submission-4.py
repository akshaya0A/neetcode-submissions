# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast=fast.next.next
        mid = slow.next
        slow.next = None
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev
        mid = reverse(mid)
        first = head
        while mid:
            temp1 = first.next
            temp2 = mid.next
            first.next = mid
            mid.next = temp1
            first = temp1
            mid = temp2
     

