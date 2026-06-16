# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        dummy = ListNode(0, head)
        curr = head
        i =0
        while curr:
            curr = curr.next
            i +=1
        length = i - n
        curr = dummy
        while curr and length >0:
            curr = curr.next
            length -=1
        curr.next = curr.next.next
        return dummy.next