# Problem: Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/description/

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = [0]*(target+1)
        memo[0]=0
        for num in nums:
            if num<=target:
                memo[num] = 1

        for i in range(1, len(memo)):
            for j in nums:
                if i>j:
                    memo[i]+=memo[i-j]

        return memo[target]