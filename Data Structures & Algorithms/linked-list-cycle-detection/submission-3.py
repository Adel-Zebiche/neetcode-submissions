# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dico = {}
        while head :
            if head in dico :
                return True
            else :
                dico[head] = head.next
            head=head.next
        return False
            
        
        