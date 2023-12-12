class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        '''
        1. have a dictionary with frequesncy
        2. we will have visited set 
        3. diclength for each of new start and the length we got from them as value
        4. we will do dfs traversal for left and right of the the cur item of the sums  cheking visited and existence in the frequency
        5. return tha max vlaue of diclenth dictionary
        '''
        if len(nums) == 0:
            return 0 
        n = Counter(nums)
        visited =set()
        diclength = defaultdict(int)

        def dfs(cur, item):
            visited.add(item)
            left =  item -1
            right = item + 1
            diclength [cur] += 1
            if left in n and left not in visited:
                dfs(cur,left )
            if right in n and  right not in visited:
                dfs(cur,right)
        for val in nums:
            if val not in visited :
                dfs(val, val)
        return max(diclength.values())



        

