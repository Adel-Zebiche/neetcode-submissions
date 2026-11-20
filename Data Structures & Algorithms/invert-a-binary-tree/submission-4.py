# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root :
            return
        l, r = root.left, root.right
        if r :
            root.left = r
        else :
            root.left = None
        if l :
            root.right = l
        else :
            root.right = None
        self.invertTree(r)
        self.invertTree(l)
        return root