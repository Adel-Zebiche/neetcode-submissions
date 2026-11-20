# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dico = {}
        def maxDepth(node) :
            
            if node not in dico : 
                if not node.right and not node.left :
                    dico[node] = 0
                else :
                    cdd_droit = (maxDepth(node.right) + 1) if node.right else 0
                    cdd_gauche = (maxDepth(node.left) + 1) if node.left else 0
                    dico[node] = max(cdd_gauche, cdd_droit)
            return dico[node]
        maxDepth(root)
        stack = deque([root])
        maxi = 0
        while stack :
            node = stack.popleft()
            result = 0
            if node.right :
                result = result + 1 + dico[node.right]
                stack.append(node.right) 
            if node.left :
                result = result + 1 + dico[node.left]
                stack.append(node.left) 
            maxi = max(maxi, result)
        return maxi




        
    




