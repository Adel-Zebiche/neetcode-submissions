# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dico = {}
        maxi = 0
        def maxDepth(node) :
            nonlocal maxi
            if not node :
                return 0
            l, r = maxDepth(node.left), maxDepth(node.right)
            maxi = max(l+r, maxi)
            return 1 + max(l,r)

        maxDepth(root)
        return maxi




        
    




