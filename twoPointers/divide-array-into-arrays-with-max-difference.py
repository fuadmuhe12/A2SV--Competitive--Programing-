class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) < 3:
            return []
        else:
            nums.sort()
            ans = []
            start = 0
            for i in range(2,len(nums),3 ):
                if nums[i] - nums[start]> k:
                    return []
                else:
                    ans.append(nums[start:i+1])
            
                start += 3
            return ans

