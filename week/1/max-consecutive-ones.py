class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start  = 0
        end = 0
        mx= 0
        while end < len(nums):
            if nums[end] == 1:
                mx = max(mx, end -start +1)
                end += 1
            else:
                if end == start:
                    start += 1
                    end += 1
                else:
                    end += 1
                    start = end
            
        return mx

                

            