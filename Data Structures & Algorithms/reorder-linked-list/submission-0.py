# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        queue_start, queue_end = deque([]), deque([])
        slow = head
        fast = head.next
        while fast and fast.next :
            slow = slow.next
            queue_start.appendleft(slow)
            fast = fast.next.next
            
        while slow.next :
            queue_end.append(slow.next)
            slow = slow.next
        current = head
        while queue_end  :
            current.next = queue_end.pop()
            current = current.next
            if queue_start :
                current.next= queue_start.pop()
                current = current.next
        current.next = None
        return None

        