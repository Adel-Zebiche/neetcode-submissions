# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pt1 = pt2 = head
        while pt2 :
            if not pt2.next :
                return False
            pt2 = pt2.next.next
            pt1 = pt1.next
            if pt1 == pt2 :
                return True
        return False
            
  
            
        
        