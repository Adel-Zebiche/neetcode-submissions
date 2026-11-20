"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head :
            return
        dico = {None : None}
        stack = [head]
        first_found = False
        while stack :
            node = stack.pop()
            if node not in dico :
                val, suiv, rdm = node.val, node.next, node.random
                head2 = Node(val)
                if suiv != None :
                    if suiv not in dico and suiv not in stack:
                        stack.append(suiv)
                if rdm != None:
                    if rdm not in dico and rdm not in stack:
                        stack.append(rdm)
                dico[node] = head2

        for key in dico :
            if key :
                dico[key].next = dico[key.next]
                dico[key].random = dico[key.random]
        return dico[head]
        

        