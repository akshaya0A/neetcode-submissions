class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            k -= 1
            
            if k == 0:
                return node.val
            
            root = node.right