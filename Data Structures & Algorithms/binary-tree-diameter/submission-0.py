# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0
            
            return 1 + max(dfs(node.right), dfs(node.left))
        
        diameter = dfs(root.right) + dfs(root.left)
        subd = max(self.diameterOfBinaryTree(root.right), self.diameterOfBinaryTree(root.left))
        
        return max(diameter, subd)





