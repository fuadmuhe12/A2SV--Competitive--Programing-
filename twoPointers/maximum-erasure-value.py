class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        '''
     what do we need : two pointer (start = 0, end = 0) counter map(count = defaultdict(int)) 

                       for while loop , for over the value , while to contract untill evey subarry value
                       is one


        '''
        start = 0  
        # end = 0 no needed to create the value as we use for loop
        count = defaultdict(int)
        sums = 0
        mx = 0

        for end , val in enumerate(nums):
            count[val] += 1
            sums += val

            if count[val] > 1:
                while count[val] !=  1:
                    sums -= nums[start]
                    count[nums[start]] -= 1
                    start += 1
            mx = max(mx, sums)
        return mx

                    
                    

        
