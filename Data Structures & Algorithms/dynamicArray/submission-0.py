class DynamicArray:
    
    array = [None]
    capacity = 1
    size = 0
    pushIdx = 0
    popIdx = -1
    def __init__(self, capacity: int):
        self.array = self.array * capacity
        self.capacity = capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.set(self.pushIdx, n)
        self.pushIdx = self.pushIdx + 1
        self.popIdx = self.popIdx + 1
        self.size = self.size + 1

    def popback(self) -> int:
        lastElement = self.get(self.popIdx)
        self.pushIdx = self.pushIdx - 1
        self.popIdx = self.popIdx - 1
        self.size = self.size - 1
        return lastElement

    def resize(self) -> None:
        extensionArray = [None] * self.capacity
        self.array = self.array + extensionArray
        self.capacity = self.capacity * 2

    def getSize(self) -> int:
        return self.size
        
    def getCapacity(self) -> int:
        return self.capacity