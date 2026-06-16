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
        my_map = {None:None}
        curr = head
        while curr:
            my_map[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            copy = my_map[curr]
            copy.next = my_map[curr.next]
            copy.random = my_map[curr.random]
            curr = curr.next
        return my_map[head]