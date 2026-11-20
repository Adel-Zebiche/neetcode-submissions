# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dico = {}
        cpt = 0
        prev = None
        output = head
        while head :
            dico[cpt] = (prev,head)
            prev = head
            head = head.next
            cpt+=1
        
        prev, current = dico[cpt-n]
        if prev == None :
            # proch = output.next
            # current.next = None
            return current.next
        else :
            prev.next = current.next
            current.next = None
        return output
        
            
        
        