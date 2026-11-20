# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        mid = slow 

        
        current = mid.next
        mid.next = None
        prev = None
        while current :
            proch = current.next
            current.next = prev
            prev = current
            current = proch

        current_2 = prev
        
        
        
        current_1 = head.next
        while head != mid :
            head.next = current_2
            head = head.next
            current_2 = current_2.next

            head.next = current_1
            head = head.next
            current_1 = current_1.next
        if current_2 :
            head.next = current_2
        return None

        