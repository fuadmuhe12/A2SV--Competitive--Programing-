class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        1.sort the poeple based on therir weight and have left and right pointer while the  right is >= left
        if the sum of two is equal to the weight move insed increase the bot else move the right only
                    '''
        l = 0
        r =  len(people)-1
        people.sort()
        tot = 0
        while r >=l:
            if people [r] + people[l] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            tot += 1
        return tot


