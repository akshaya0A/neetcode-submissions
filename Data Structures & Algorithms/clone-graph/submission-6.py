"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        copy = {}
        return self.helper(node, copy)
    
    def helper(self, node, copy):
        if node in copy:
            return copy[node]
        num = Node(node.val)
        copy[node] = num
        for neigh in node.neighbors:
            num.neighbors.append(self.helper(neigh, copy))
        return num    
