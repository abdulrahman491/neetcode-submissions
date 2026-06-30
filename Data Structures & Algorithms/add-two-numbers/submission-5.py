# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        temp1 = l1
        temp2 = l2
        addNum = temp1.val + temp2.val
        newNode = None
        old = None
        newHead = None
        carry = 0
        if addNum <= 9:
            newNode = ListNode(addNum)
            old = newNode
            newHead = newNode
        else: 
            if addNum == 10:
                newNode = ListNode(0)
                carry = 1
                newHead = newNode
                old = newNode
            elif addNum == 11:
                newNode = ListNode(1)

                carry = 1
                newHead = newNode
                old = newNode
            elif addNum == 12:
                newNode = ListNode(2)
                carry = 1
                newHead = newNode
                old = newNode
            elif addNum == 13:
                newNode = ListNode(3)
                carry = 1
                newHead = newNode
                old = newNode
            elif addNum == 14:
                newNode = ListNode(4)
                carry = 1
                newHead = newNode
                old = newNode
            elif addNum == 15:
                newNode = ListNode(5)
                carry = 1
                newHead = newNode
                old = newNode
            elif addNum == 16:
                newNode = ListNode(6)
                carry = 1
                newHead = newNode
                old = newNode
            elif addNum == 17:
                newNode = ListNode(7)
                carry = 1
                newHead = newNode
                old = newNode
            elif addNum == 18:
                newNode = ListNode(8)
                carry = 1
                newHead = newNode
                old = newNode
            elif addNum == 19:
                newNode = ListNode(9)
                carry = 1
                newHead = newNode
                old = newNode
        temp1 = temp1.next
        temp2 = temp2.next
        while temp1 is not None and temp2 is not None:
            addNum = temp1.val + temp2.val + carry
            if addNum <= 9:
                newNode = ListNode(addNum)
                old.next = newNode
                old = newNode
                temp1 = temp1.next
                temp2 = temp2.next
                carry = 0
            else: 
                if addNum == 10:
                    newNode = ListNode(0)
                    carry = 1
                    old.next = newNode
                    old = newNode
                    temp1 = temp1.next
                    temp2 = temp2.next
                elif addNum == 11:
                    newNode = ListNode(1)
                    carry = 1
                    old.next = newNode
                    old = newNode
                    temp1 = temp1.next
                    temp2 = temp2.next
                elif addNum == 12:
                    newNode = ListNode(2)
                    carry = 1
                    old.next = newNode
                    old = newNode
                    temp1 = temp1.next
                    temp2 = temp2.next
                elif addNum == 13:
                    newNode = ListNode(3)
                    carry = 1
                    old.next = newNode
                    old = newNode
                    temp1 = temp1.next
                    temp2 = temp2.next
                elif addNum == 14:
                    newNode = ListNode(4)
                    carry = 1
                    old.next = newNode
                    old = newNode
                    temp1 = temp1.next
                    temp2 = temp2.next
                elif addNum == 15:
                    newNode = ListNode(5)
                    carry = 1
                    old.next = newNode
                    old = newNode
                    temp1 = temp1.next
                    temp2 = temp2.next
                elif addNum == 16:
                    newNode = ListNode(6)
                    carry = 1
                    old.next = newNode
                    old = newNode
                    temp1 = temp1.next
                    temp2 = temp2.next
                elif addNum == 17:
                    newNode = ListNode(7)
                    carry = 1
                    old.next = newNode
                    old = newNode
                    temp1 = temp1.next
                    temp2 = temp2.next
                elif addNum == 18:
                    newNode = ListNode(8)
                    carry = 1
                    old.next = newNode
                    old = newNode
                    temp1 = temp1.next
                    temp2 = temp2.next
                elif addNum == 19:
                    newNode = ListNode(9)
                    carry = 1
                    old.next = newNode
                    old = newNode
                    temp1 = temp1.next
                    temp2 = temp2.next

        while temp1 is not None:
            addNum = temp1.val + carry 
            if addNum <= 9:
                newNode = ListNode(addNum)
                old.next = newNode
                old = newNode
                carry = 0
                temp1 = temp1.next
            elif addNum == 10:
                newNode = ListNode(0)
                carry = 1
                old.next = newNode
                old = newNode
                temp1 = temp1.next

            
        while temp2 is not None:
            addNum = temp2.val + carry 
            if addNum <= 9:
                newNode = ListNode(addNum)
                old.next = newNode
                old = newNode
                carry = 0
                temp2 = temp2.next
            elif addNum == 10:
                newNode = ListNode(0)
                carry = 1
                old.next = newNode
                old = newNode
                temp2 = temp2.next

        if carry == 1:
            newNode = ListNode(1)
            old.next = newNode


        return newHead

