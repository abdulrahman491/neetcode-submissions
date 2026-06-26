# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if (list1 is None) and (list2 is None):
            return None

        if list1 is None:
            return list2
        
        if list2 is None:
            return list1

        trav1 = list1
        trav2 = list2
        head3 = None
        if trav1.val <= trav2.val:
            head3 = ListNode(trav1.val)
            trav1 = trav1.next
        else:
            head3 = ListNode(trav2.val)
            trav2 = trav2.next
        trav3 = head3
        prev = head3
        while (trav1 is not None) and (trav2 is not None): 
            if trav1.val <= trav2.val:
                trav3 = ListNode(trav1.val)
                trav1 = trav1.next
                prev.next = trav3
                prev = trav3
            else:
                trav3 = ListNode(trav2.val)
                trav2 = trav2.next
                prev.next = trav3
                prev = trav3
        
        if trav1 is not None:
            while trav1 is not None:
                trav3 = ListNode(trav1.val)
                trav1 = trav1.next
                prev.next = trav3
                prev = trav3
        else:
            while trav2 is not None:
                trav3 = ListNode(trav2.val)
                trav2 = trav2.next
                prev.next = trav3
                prev = trav3

        return head3