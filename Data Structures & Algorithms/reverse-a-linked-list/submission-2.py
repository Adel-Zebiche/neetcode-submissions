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
        proch = current.next
        while proch :
            current.next = prev
            prev = current
            current = proch
            proch = proch.next
        current.next = prev
        dummy = ListNode()
        dummy.next = current
        head.next = None
        return dummy.next

        