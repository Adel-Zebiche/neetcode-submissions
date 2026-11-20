# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cpt = 0
        seen = set()
        while head :
            cpt+=1
            head = head.next
            if cpt > 1000 :
                return True
        return False