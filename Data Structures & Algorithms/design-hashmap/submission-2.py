class MyHashMap:

    def __init__(self):
        self.maxNum = 1000001
        self.hashMap = [None] * self.maxNum
        

    def put(self, key: int, value: int) -> None:
            self.hashMap[key] = (key, value)

    def get(self, key: int) -> int:
        if self.hashMap[key] != None:
            return self.hashMap[key][1]
        else:
            return -1

    def remove(self, key: int) -> None:
        if self.hashMap[key] != None:
            self.hashMap[key] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)