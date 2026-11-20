# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        mini, maxi = min(p.val, q.val), max(p.val, q.val)
        while True :
            if maxi < root.val :
                root = root.left
            elif mini > root.val :
                root = root.right
            else :
                return root
            
