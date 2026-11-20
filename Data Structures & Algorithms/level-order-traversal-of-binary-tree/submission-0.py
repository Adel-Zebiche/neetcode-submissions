# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        L = []
        queue = deque([(root,0)])
        while queue :
            node, idx = queue.pop()
            if node.left :
                queue.appendleft((node.left, idx+1))
            if node.right :
                queue.appendleft((node.right, idx+1))
            if len(L) == idx :
                L.append([node.val])
            else :
                L[idx].append(node.val)
        return L
            
