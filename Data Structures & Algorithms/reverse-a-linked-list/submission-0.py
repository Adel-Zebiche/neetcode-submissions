# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if not head :
            return 
        L = [head.val]
        while current.next :
            L.append(current.next.val)
            current = current.next
        dummy = ListNode()
        actuel = dummy
        for i in range(len(L)-1, -1, -1) :
            actuel.next = ListNode(L[i])
            actuel = actuel.next
        return dummy.next


        