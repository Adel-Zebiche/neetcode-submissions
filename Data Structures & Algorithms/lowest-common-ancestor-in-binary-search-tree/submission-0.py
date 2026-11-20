# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        dico = {root : None}
        stack = deque([root])
        while stack :
            node = stack.pop()
            if node.right :
                dico[node.right] = node
                stack.append(node.right)
            if node.left :
                dico[node.left] = node
                stack.append(node.left)
        set1 = set()
        while p :
            set1.add(p)
            p = dico[p]
        while q :
            if q in set1 :
                return q
            q = dico[q]
        



            