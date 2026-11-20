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
            if node not in dico : 
                if not node.right and not node.left :
                    dico[node] = 0
                else :
                    cdd_droit = (maxDepth(node.right) + 1) if node.right else 0
                    cdd_gauche = (maxDepth(node.left) + 1) if node.left else 0
                    diametre = cdd_droit + cdd_gauche
                    maxi = max(diametre, maxi)
                    dico[node] = max(cdd_gauche, cdd_droit)
            return dico[node]
        maxDepth(root)
        
        return maxi




        
    




