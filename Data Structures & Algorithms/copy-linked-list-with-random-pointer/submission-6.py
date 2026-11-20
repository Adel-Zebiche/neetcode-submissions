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
    
        dico = {None : None}
        current = head
        while current :
            val = current.val
            dico[current] = Node(val)
            current = current.next
            
        for key in dico :
            if key :
                dico[key].next = dico[key.next]
                dico[key].random = dico[key.random]
        return dico[head]
        

        