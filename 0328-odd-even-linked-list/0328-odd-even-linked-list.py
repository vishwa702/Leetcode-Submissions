# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        odds = head
        if head.next: 
            evens = head.next


        o, e = odds, evens

        while e.next or o.next:
            if e.next:
                if e.next == o:
                    e.next = None
                    o.next = evens
                    break
                o.next = e.next
                o = o.next
            
            if o.next:
                if o.next == e:
                    o.next = evens
                    break
                e.next = o.next
                e = e.next
        
        return head