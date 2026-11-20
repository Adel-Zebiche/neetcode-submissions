# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        output = True
        def height(node) :
            nonlocal output
            if not node :
                return 0
            l, r = height(node.left), height(node.right)
            if not (-1 <= r-l <= 1) :
                output = False
            return 1 + max(l, r)

        height(root)
        return output
