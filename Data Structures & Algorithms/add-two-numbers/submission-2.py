# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        retenue = 0
        while l1 or l2 :
            if l1 :
                if l2 :
                    som = l1.val+l2.val + retenue
                    l2 = l2.next
                else :
                    som = l1.val + retenue
                l1 = l1.next
            else :
                som = l2.val + retenue
                l2 = l2.next
            retenue = som//10
            prev.next = ListNode(som%10)
            prev = prev.next
        if retenue :
            prev.next = ListNode(1)
        return dummy.next
        