# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        mini, maxi = min(p.val, q.val), max(p.val, q.val)
        node = root
        while True :
            if maxi < node.val :
                node = node.left
            elif mini > node.val :
                node = node.right
            else :
                return node
            
