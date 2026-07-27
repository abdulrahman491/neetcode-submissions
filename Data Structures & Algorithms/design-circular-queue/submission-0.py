class ListNode:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.used = 0
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.head == None:
                self.head = ListNode(val=value)
                self.tail = self.head
                self.used += 1
            else:
                node = ListNode(val=value)
                node.prev = self.tail
                node.next = None
                self.tail.next = node
                self.tail = node
                self.used += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            if self.head.next == None:
                self.head = None
                self.tail = self.head
                self.used -= 1
            else:
                self.head = self.head.next 
                self.head.prev = None
                self.used -= 1
        return True
            
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.head.val
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else: 
            return self.tail.val
        

    def isEmpty(self) -> bool:
        return self.head == None
        

    def isFull(self) -> bool:
        return self.used == self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()