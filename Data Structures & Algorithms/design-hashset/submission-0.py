class MyHashSet:

    def __init__(self):
        self.maxNum = 1000000
        self.hashSet = [None] * self.maxNum

    def add(self, key: int) -> None:
        if self.hashSet[key] is None:
            self.hashSet[key] = key

    def remove(self, key: int) -> None:
        if self.hashSet[key] is not None:
            self.hashSet[key] = None

    def contains(self, key: int) -> bool:
        return self.hashSet[key] != None


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)