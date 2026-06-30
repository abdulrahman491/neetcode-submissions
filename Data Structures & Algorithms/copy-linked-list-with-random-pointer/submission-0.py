"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':


        
        if head is None:
            return head

        temp = head
        listMap = []
        while temp is not None:
            if temp.random is None:
                listMap.append(None)
                temp = temp.next
            else:
                checker = head
                idx = 0
                while checker != temp.random:
                    checker = checker.next
                    idx = idx + 1
                listMap.append(idx)
                temp = temp.next

        temp = head
        newNode = Node(temp.val)
        newHead = newNode
        old = newNode
        temp = temp.next

        while temp is not None:
            newNode = Node(temp.val)
            old.next = newNode
            old = newNode
            temp = temp.next

        temp = newHead

        idx = 0
        while temp is not None:
            if listMap[idx] is None:
                temp.random = None
                idx = idx + 1
                temp = temp.next
            else:
                listPtr = newHead
                listIdx = 0
                while listIdx != listMap[idx]:
                    listPtr = listPtr.next
                    listIdx = listIdx + 1
                
                temp.random = listPtr
                idx = idx + 1
                temp = temp.next

        return newHead
            