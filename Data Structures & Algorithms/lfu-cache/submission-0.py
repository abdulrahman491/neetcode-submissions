class ListNode:
    def __init__(self, val=None, key=None, counter=None, next=None, prev=None):
        self.val = val
        self.key = key 
        self.counter = counter
        self.next = next
        self.prev = prev

class LFUCache:



    def __init__(self, capacity: int):
        self.hashMain = {}
        self.hashHeads = {}
        self.hashTails = {}

        self.capacity = capacity
        self.minCounter = 300000
        

    def get(self, key: int) -> int:
        if key not in self.hashMain:
            return -1

        oldCounter = self.hashMain[key].counter
        newCounter = oldCounter + 1
        self.hashMain[key].counter = newCounter

        #Delete the element from old counter hash
        if self.hashHeads[oldCounter] == self.hashTails[oldCounter]:
            del self.hashHeads[oldCounter]
            del self.hashTails[oldCounter]
            self.minCounter = newCounter
        elif self.hashHeads[oldCounter] == self.hashMain[key]:
            self.hashHeads[oldCounter] = self.hashHeads[oldCounter].next
            self.hashHeads[oldCounter].prev = None
        elif self.hashTails[oldCounter] == self.hashMain[key]:
            self.hashTails[oldCounter] = self.hashTails[oldCounter].prev
            self.hashTails[oldCounter].next = None
        else:
            self.hashMain[key].prev.next = self.hashMain[key].next
            self.hashMain[key].next.prev = self.hashMain[key].prev

        #Insert the deleted Item in the new counter hash

        if newCounter not in self.hashHeads:
            self.hashHeads[newCounter] = self.hashMain[key]
            self.hashTails[newCounter] = self.hashMain[key]
            self.hashMain[key].next = None
            self.hashMain[key].prev = None
        else:
            self.hashMain[key].next = None
            self.hashMain[key].prev = self.hashTails[newCounter]
            self.hashTails[newCounter].next = self.hashMain[key]
            self.hashTails[newCounter] = self.hashMain[key]

        return self.hashMain[key].val


    def put(self, key: int, value: int) -> None:

        if key not in self.hashMain:
            if len(self.hashMain) < self.capacity:
                self.minCounter = 1
                if 1 not in self.hashHeads:
                    self.hashHeads[1] = ListNode(val=value, key=key, counter=1)
                    self.hashTails[1] = self.hashHeads[1]
                    self.hashMain[key] = self.hashHeads[1]
                else:
                    self.hashTails[1].next = ListNode(val=value, key=key, counter=1, prev = self.hashTails[1])
                    self.hashTails[1] = self.hashTails[1].next
                    self.hashMain[key] = self.hashTails[1]

            else:
                #Deleting an element
                if self.hashHeads[self.minCounter] == self.hashTails[self.minCounter]:
                    del self.hashMain[self.hashHeads[self.minCounter].key]
                    del self.hashTails[self.minCounter]
                    del self.hashHeads[self.minCounter]

                else:
                    del self.hashMain[self.hashHeads[self.minCounter].key]
                    self.hashHeads[self.minCounter] = self.hashHeads[self.minCounter].next
                    self.hashHeads[self.minCounter].prev = None

                self.minCounter = 1

                #Inserting an Element
                if 1 not in self.hashHeads:
                    self.hashHeads[1] = ListNode(val=value, key=key, counter=1)
                    self.hashTails[1] = self.hashHeads[1]
                    self.hashMain[key] = self.hashHeads[1]
                else:
                    self.hashTails[1].next = ListNode(val=value, key=key, counter=1, prev = self.hashTails[1])
                    self.hashTails[1] = self.hashTails[1].next
                    self.hashMain[key] = self.hashTails[1]


        else:
            oldCounter = self.hashMain[key].counter
            newCounter = oldCounter + 1
            self.hashMain[key].val = value
            self.hashMain[key].counter = newCounter

            #Delete the element from old counter hash
            if self.hashHeads[oldCounter] == self.hashTails[oldCounter]:
                del self.hashHeads[oldCounter]
                del self.hashTails[oldCounter]
                self.minCounter = newCounter
            elif self.hashHeads[oldCounter] == self.hashMain[key]:
                self.hashHeads[oldCounter] = self.hashHeads[oldCounter].next
                self.hashHeads[oldCounter].prev = None
            elif self.hashTails[oldCounter] == self.hashMain[key]:
                self.hashTails[oldCounter] = self.hashTails[oldCounter].prev
                self.hashTails[oldCounter].next = None
            else:
                self.hashMain[key].prev.next = self.hashMain[key].next
                self.hashMain[key].next.prev = self.hashMain[key].prev

            #Insert the deleted Item in the new counter hash

            if newCounter not in self.hashHeads:
                self.hashHeads[newCounter] = self.hashMain[key]
                self.hashTails[newCounter] = self.hashMain[key]
                self.hashMain[key].next = None
                self.hashMain[key].prev = None
            else:
                self.hashMain[key].next = None
                self.hashMain[key].prev = self.hashTails[newCounter]
                self.hashTails[newCounter].next = self.hashMain[key]
                self.hashTails[newCounter] = self.hashMain[key]
            








# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)