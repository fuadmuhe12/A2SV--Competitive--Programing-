class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #we gonna use recursion 
        nums.sort()
        close  = float('inf')
        smallsum = float('inf')
        # sums = 0
        def ksum(start, k, target):
            nonlocal close
            nonlocal smallsum
            if k != 2:
                for i in range(start, len(nums) -k+1):
                    # sums += nums[i]
                    start = i+1
                    ksum(start, k-1, target - nums[i])
                    # sums -= nums[i]
            else:
                l = start
                r = len(nums) - 1
                while r > l :
                    cur =  nums[r]+ nums[l]
                    if abs(cur-target) < close:
                        close  = min(close, abs(cur-target))
                        smallsum = cur +nums[start -1]
                    if cur  > target:
                        r -= 1
                    elif cur < target:
                        l += 1
                    else:
                        return 0
        ksum(0, 3, target)
        return smallsum
        

