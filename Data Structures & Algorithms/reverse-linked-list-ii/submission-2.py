# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head
        

        beforeFirst = None 
        first = None
        last = None

        if left > 1:
            beforeFirst = head
            first = beforeFirst.next

            count = left - 2
            while count:
                beforeFirst = beforeFirst.next 
                first = first.next
                count -= 1
        elif left == 1:
            first = head



        prevNode = first
        currNode = prevNode.next
        nextNode = currNode.next

        count = right - left - 1
        while count:
            currNode.next = prevNode

            prevNode = currNode
            currNode = nextNode
            nextNode = nextNode.next
            count -= 1
        
        currNode.next = prevNode
        last = currNode
        
        if beforeFirst != None:
            beforeFirst.next = last
        else:
            head = last

        first.next = nextNode

        
        return head