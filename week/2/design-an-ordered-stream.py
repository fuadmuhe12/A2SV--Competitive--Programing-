class OrderedStream:
    '''
    1. initiate a list in the object with size of n+1 and put 0 in each of the place 
                1. have a ptr variable starting from 0

    2. on the insert:

            2. insert values  adn at the index
                create ans= []

                do while the val os list is not zero 
                 and add to ans
                 and return ans


    '''

    def __init__(self, n: int):
        self.store = [0]*(n+1)
        self.ptr = 0

        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.store[idKey-1] = value
        ans = []
        while self.store[self.ptr] != 0:
            ans.append(self.store[self.ptr])
            self.ptr += 1
        return ans
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)