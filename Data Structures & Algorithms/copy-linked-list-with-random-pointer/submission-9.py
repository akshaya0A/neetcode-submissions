"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        copy = {}
        curr = head
        while curr:    
            copy[curr] = Node(curr.val)
            curr = curr.next
        
        curr2 = head
        while curr2:
            copy[curr2].next = copy.get(curr2.next)
            copy[curr2].random = copy.get(curr2.random)
            curr2 = curr2.next
        return copy[head]
