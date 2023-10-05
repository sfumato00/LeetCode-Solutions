class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.arr)
        self.arr += [val]
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        i = self.map[val]
        k = self.arr.pop()
        if i < len(self.arr):
            self.arr[i] = k
            self.map[k] = i
        self.map.pop(val)
        return True

    def getRandom(self) -> int:
        return self.arr[random.randrange(0, len(self.arr))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
