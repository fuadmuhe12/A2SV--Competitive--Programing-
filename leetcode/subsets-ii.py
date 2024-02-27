class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set([])
        def backtrack(temp, ind):
            if ind >= len(nums):
                return 
            cur = ind
            for i in nums[ind:]:
               
                temp.append(i)

                ans.add(tuple(sorted(temp)))
                backtrack(temp, cur + 1)

                temp.remove(i)
                cur += 1
        backtrack([], 0)
        ans  = (list(map(list, ans)))
        ans.append([])
        return ans



            