class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ans = []
        def backtrack(temp, ind, left_sum ):
            if left_sum == 0 and len(temp) == k:
                ans.append(temp[:])
                return 
            if len(temp) >= k or ind >= 9:
                return 
            cur = ind
            for i in range(ind, 9):
                temp.append(nums[i])
                left_sum -= nums[i]
                backtrack(temp, i +1, left_sum)
                temp.pop()
                left_sum += nums[i]
        backtrack([], 0, n)
        return ans
            