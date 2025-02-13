# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None

        l, r = head, head.next
        

        while r.next is not None and r.next.next is not None:
            r = r.next.next
            l = l.next
        
        l.next = l.next.next

        return head


        return None