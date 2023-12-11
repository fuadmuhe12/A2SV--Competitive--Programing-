class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        cur_ev_sum = 0 
        for  val in (nums):
            if val % 2==0:
                cur_ev_sum += val

        ans = []
        
        for add, ix in queries:
            isod = True
            cur_val = nums[ix]
            nums[ix] += add
            if cur_val % 2 == 0:
                isod = False
            if nums[ix] % 2 ==0 and not isod:
                cur_ev_sum += add 
                ans.append(cur_ev_sum)
            elif nums[ix] % 2 and not isod:
                cur_ev_sum -= cur_val
                ans.append(cur_ev_sum)
            elif nums[ix] % 2 and isod:
                ans.append(cur_ev_sum)
            elif nums[ix] % 2 == 0 and isod:
                cur_ev_sum += nums[ix]
                ans.append(cur_ev_sum)

            
        return ans
            



