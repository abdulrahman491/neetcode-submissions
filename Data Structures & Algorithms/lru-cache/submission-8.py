class ListNode:
    def __init__(self, value=None, key=None, next=None, prev=None):
        self.value = value
        self.key = key
        self.next = next
        self.prev = prev


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.tail = None
        self.head = None
        self.hashMap = {}

    def get(self, key: int) -> int:
        if key in self.hashMap:
            if self.hashMap[key] == self.tail:
                return self.hashMap[key].value
            if self.hashMap[key] == self.head:
                self.head = self.head.next
                self.head.prev = None
                self.hashMap[key].prev = self.tail
                self.hashMap[key].next = None
                self.tail.next = self.hashMap[key]
                self.tail = self.hashMap[key]
                return self.hashMap[key].value
            self.hashMap[key].prev.next = self.hashMap[key].next
            self.hashMap[key].next.prev = self.hashMap[key].prev
            self.hashMap[key].prev = self.tail
            self.hashMap[key].next = None
            self.tail.next = self.hashMap[key]
            self.tail = self.hashMap[key]
            return self.hashMap[key].value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.hashMap:
            if self.hashMap[key] == self.tail:
                self.hashMap[key].value = value
                return
            if self.hashMap[key] == self.head:
                self.head = self.head.next
                self.head.prev = None
                self.hashMap[key].prev = self.tail
                self.hashMap[key].next = None
                self.tail.next = self.hashMap[key]
                self.tail = self.hashMap[key]
                self.hashMap[key].value = value
                return
            self.hashMap[key].prev.next = self.hashMap[key].next
            self.hashMap[key].next.prev = self.hashMap[key].prev
            self.hashMap[key].prev = self.tail
            self.hashMap[key].next = None
            self.tail.next = self.hashMap[key]
            self.tail = self.hashMap[key]
            self.hashMap[key].value = value
        else:
            if len(self.hashMap) < self.capacity:
                if len(self.hashMap) == 0:
                    node = ListNode(value=value, key=key)
                    self.head = node
                    self.tail = node
                    self.hashMap[key] = node
                    return
                node = ListNode(value=value, key=key, prev=self.tail)
                self.tail.next = node
                self.tail = node
                self.hashMap[key] = node
            else: 
                if self.capacity == 1:
                    del self.hashMap[self.head.key]
                    node = ListNode(value=value, key=key)
                    self.head = node
                    self.tail = node
                    self.hashMap[key] = node
                    return
                del self.hashMap[self.head.key]
                self.head = self.head.next
                self.head.prev = None

                node = ListNode(value=value, key=key, prev=self.tail)
                self.tail.next = node
                self.tail = node
                self.hashMap[key] = node
                
