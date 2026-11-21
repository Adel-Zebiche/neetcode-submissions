# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        liste = [(root, -1000000000, 1000000000)]
        while liste :
            node, mini, maxi = liste.pop()
            if not (mini < node.val < maxi) :
                return False

            if node.right :
                liste.append((node.right, node.val, maxi))
            if node.left :
                liste.append((node.left, mini, node.val))
            
        return True


                