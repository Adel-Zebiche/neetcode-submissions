# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        liste = [(root, None, None)]
        while liste :
            node, mini, maxi = liste.pop()
            if (mini is not None and not (mini < node.val)) or (maxi is not None and not (maxi > node.val)) :
                return False
            if node.right :
                liste.append((node.right, node.val, maxi))
            if node.left :
                liste.append((node.left, mini, node.val))
            
        return True


                