# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cpt = 1
        first = head
        while head:
            if cpt <= n :
                prev, current = None, first
            else :
                prev, current = current, current.next
            head = head.next
            cpt+=1
    
        if not prev  :
            return first.next
        else :
            prev.next = current.next
            return first
        
            
        
        