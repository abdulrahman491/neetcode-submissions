class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used = 0
        self.timer = -1
        self.memory = [None for _ in range(1001)]

    def get(self, key: int) -> int:
        if self.memory[key] != None:
            self.timer += 1
            self.memory[key]['timer'] = self.timer
            return self.memory[key]['val']
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if self.memory[key] != None:
            self.timer += 1
            self.memory[key]['val'] = value
            self.memory[key]['timer'] = self.timer
        else:
            if self.used < self.capacity:
                self.timer += 1
                self.memory[key] = {'val': value, 'timer': self.timer}
                self.used += 1
            else: 
                minTimer = None
                minTimerKey = None

                idx = 0
                while idx < len(self.memory):
                    if self.memory[idx] != None:
                        minTimer = self.memory[idx]['timer']
                        minTimerKey = idx
                        idx += 1
                        break
                    idx += 1
                while idx < len(self.memory):
                    if self.memory[idx] != None and self.memory[idx]['timer'] < minTimer:
                        minTimer = self.memory[idx]['timer']
                        minTimerKey = idx
                    idx += 1
                
                self.timer += 1
                self.memory[minTimerKey] = None
                self.memory[key] = {'val': value, 'timer': self.timer}
                
