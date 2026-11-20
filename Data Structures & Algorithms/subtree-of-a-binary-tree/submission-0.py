# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSub(p, q) :
            if not p and not q :
                return True
            if not p or not q :
                return False
            return p.val == q.val and isSub(p.right, q.right) and isSub(p.left, q.left)
        stack = [root]
        while stack :
            noeud = stack.pop()
            if isSub(noeud, subRoot) :
                return True
            if noeud.right :
                stack.append(noeud.right)
            if noeud.left :
                stack.append(noeud.left)
        return False