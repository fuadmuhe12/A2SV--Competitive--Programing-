class Solution:
    def minOperations(self, s: str) -> int:
        '''
        1. we will have two cases , 1st starting with one  2 second staring with 0 , we will check both cases and return the diffrerecnce between and which is the lowest


         '''
         #case one startting with 1
        od = '1'
        ev = '0'
        one_dirrence = 0
        zero_difference =0
        for i in range(1,  len(s)+1):
            if i%2:
                if s[i-1] == od:
                    zero_difference += 1
                else:
                    one_dirrence += 1
            else:
                if s[i-1] == ev:
                    zero_difference += 1
                else:
                    one_dirrence += 1
        return min(one_dirrence, zero_difference )



