# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return
        if not head.next :
            return ListNode(head.val)
            
        prev = head
        current = head.next
        head.next = None
        while current.next  :
            proch = current.next
            current.next = prev
            prev = current
            current = proch
            

        current.next = prev
        
        return current

        