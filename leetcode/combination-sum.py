class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(temp, left_sum, ind):
            if left_sum == 0:
                ans.append(temp[:])
                return 
            cur = ind
            for val in candidates[ind:]:
                for occurence in range(1, left_sum//val +1):
                    left_sum -= val * occurence
                    temp.append([val, occurence])
                    backtrack(temp, left_sum, cur +1)
                    left_sum += val * occurence
                    temp.pop()
                cur += 1
        backtrack([], target, 0)
        final = []
        for i in ans:
            sub = []
            for val , oc in i :
                sub.extend([val] *oc)
            final.append(sub)
        return final

