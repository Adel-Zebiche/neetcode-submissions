# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = head
        for i in range(0, n) :
            head = head.next
        prev, current = dummy, first

        while head:
            prev, current = current, current.next
            head = head.next

        prev.next = current.next
        return dummy.next
        
            
        
        