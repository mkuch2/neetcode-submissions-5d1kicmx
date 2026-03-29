# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()

        if root == None:
            return root
        
        q.append(root)

        while q:
            p = q.popleft()

            l = p.left
            r = p.right
            temp = r

            p.right = l
            p.left = temp

            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)
        
        return root


