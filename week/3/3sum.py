class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        1. create Counter
        2. create answer store in set 
        3. for i in in range len(lst) :
             for j in range(i, len(lst))
             count = 0
                val  = -(nu[i] + num[j]) 
                if val == num[i] and val = num[j]:
                    count  =  3
                if val ==num[i]:
                    count = 2
                if val == num[j]
                    count = 2
                else: 
                    count =  1
                if val in dic and value >= count:
                    ans.adde(sorted([val[i], val[j], v]))

assumotion  order does not matter  and set accepts list
                return 
        """
        dic = Counter(nums)
        visited =set()
        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                
                val =   -(nums[i]+ nums[j])
                if val == nums[i] and val == nums[j]:
                    count = 3
                elif val == nums[i] or val == nums[j]:
                    count = 2
                else:
                    count = 1
                if val in dic and dic[val] >= count and tuple( sorted([nums[i], nums[j], val])) not in visited:
                    ans.append(sorted([nums[i], nums[j], val]))
                    visited.add(tuple( sorted([nums[i], nums[j], val])))

        return (ans)