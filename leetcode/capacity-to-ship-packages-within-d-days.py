class Solution:
    def shipWithinDays(self, wei: List[int], days: int) -> int:
        left = max(wei)
        right = sum(wei)
        res = right
        while right >= left:
            mid = (right + left)//2
            acc = 0
            day = 1
            for i in wei:
                acc += i
                if acc > mid:
                    
                    acc = i
                    day += 1
            if day <= days:
                res = mid
                right = mid - 1
            elif day >days:
                left = mid + 1
            else:
                right = mid - 1 
        return res
                


            # if nums[mid] ==  target:
            #    res[0] = mid
            #    right = mid -1
            # elif nums[mid] >  target:
            #     right =  mid-1
            # else:
            #     left = mid +1