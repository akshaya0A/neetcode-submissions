# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val, 0)
    def dfs(self, node, max_val, count):
        if not node:
            return count
        
        if node.val >= max_val:
            count += 1
        
        max_val = max(max_val, node.val)
        
        count = self.dfs(node.left, max_val, count)
        count = self.dfs(node.right, max_val, count)
        
        return count