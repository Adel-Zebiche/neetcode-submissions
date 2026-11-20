# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cpt = 1
        first = head
        for i in range(n) :
            head = head.next
        prev, current = None, first
        
        while head:
            prev, current = current, current.next
            head = head.next

    
        if not prev  :
            return first.next
        else :
            prev.next = current.next
            return first
        
            
        
        