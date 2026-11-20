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
            dico[current] = Node(current.val)
            current = current.next
        
        current = head
        while current :
            dico[current].next = dico[current.next]
            dico[current].random = dico[current.random]
            current = current.next
        return dico[head]
        

        