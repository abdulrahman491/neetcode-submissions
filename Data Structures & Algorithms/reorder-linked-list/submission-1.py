# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None: 
            return

        curr = head
        next = curr.next
        last = None
        pLast = None
        
        while next.next is not None:
            pLast = next
            while pLast.next.next is not None:
                pLast = pLast.next
            last = pLast.next

            curr.next = last
            last.next = next
            pLast.next = None
            curr = next 
            next = next.next

            if next is None:
                return

        return 