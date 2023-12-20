class RandomizedSet:
    '''
    1. we have a set 

    '''

    def __init__(self):
        self.store = set()
        self.lst = []
        self.rem = set()

    def insert(self, val: int) -> bool:
        if val in self.store:
            return False
        else:
            self.store.add(val)
            self.lst.append(val)
            self.rem.discard(val)

            return True
        

    def remove(self, val: int) -> bool:
        if val in self.store:
            self.store.discard(val)
            self.rem.add(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        while True:
            rn = random.randint(0, len(self.lst)-1)
            if self.lst[rn] not in self.rem:
                return self.lst[rn]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()