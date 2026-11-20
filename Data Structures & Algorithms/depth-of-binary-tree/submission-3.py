# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        stack, maxi = [(root,1)], 1
        while stack :
            current, cpt = stack.pop()
            maxi = max(maxi, cpt)
            if current.right :
                stack.append((current.right, cpt+1))    
            if current.left :
                stack.append((current.left, cpt+1))
                
        return maxi