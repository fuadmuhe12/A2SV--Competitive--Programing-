class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        from itertools import accumulate
        prex=  list(accumulate(nums))
        store = 0
        mx = nums[0]
        for ind, val in enumerate(nums):
            if val <= mx:
                store = mx * (ind +1)  - prex[ind]
            else:
                if val > store :
                    val -= store
                    store = 0
                else:
                    store -= val
                    val = 0
                mx = max(math.ceil((mx * ind + val)/(ind+1)) , mx)

            store = mx * (ind +1)  - prex[ind]
        return  mx

