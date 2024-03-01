class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        def backtrack(ind, temp, leftsum):
            
            if leftsum < 0:
                return False
            if leftsum == 0:
                ans.add(tuple(sorted(temp[:])))
                return 
            count = 1
            seen = set()
            for i in candidates[ind:]:
                if i in seen:
                    count += 1
                    continue
                seen.add(i)
                leftsum -= i
                temp.append(i)
                backtrack(ind + count,temp, leftsum ) 
                leftsum += i
                temp.pop()
                count += 1
        
        backtrack(0, [], target)
        return list(map(list, ans))

