class Solution:
    def isHappy(self, n: int) -> bool:
        '''1. create a set to store an instance of a value in each 
            2. initiate  a while loop WIth True value  and 
            if the value was 1 return True 
            3. add each state to the set if it not in there else return False
            
        '''
        visited = set()
        while True :
            tot = 0
            if n in visited:
                return False
            else:
                visited.add(n)
            for i in str(n):
                tot += int(i)**2
            if tot  == 1:
                return True
            n = tot
            
                