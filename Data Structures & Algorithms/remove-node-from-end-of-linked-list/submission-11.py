# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        for i in range(0, n) :
            head = head.next
        
        while head:
            prev = prev.next
            head = head.next

        prev.next = prev.next.next
        return dummy.next
        
            
        
        