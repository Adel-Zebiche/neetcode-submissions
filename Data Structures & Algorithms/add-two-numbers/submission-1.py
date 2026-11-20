# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = l1, l2
        while l1 and l2 :
            l1 = l1.next
            l2 = l2.next
        if not l2 :
            cle, value = head1, head2
        else :
            cle, value = head2, head1
        dico = {}
        lgst, lwst = cle, value
        while lwst :
            dico[lgst] = lwst
            lgst=lgst.next
            lwst=lwst.next
        while lgst :
            dico[lgst] = ListNode(0)
            lgst = lgst.next
        dummy = ListNode()
        prev = dummy
        retenue = 0
        while cle :
            val = cle.val + dico[cle].val + retenue
            retenue = val // 10
            current = ListNode(val%10)
            prev.next = current
            prev = current
            cle = cle.next
        if retenue :
            current.next = ListNode(1)
        return dummy.next
