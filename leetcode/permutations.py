class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        used = {}
        
        def rec(arr, k = 0, temp = []):
            if k >= len(nums):
                ans.append(temp[:])
                del used[temp.pop()]
                print(temp)

                return 
            for i in arr:
                print(temp)
                if i in used:
                    continue
                temp.append(i)
                used[i] = 1
                rec(arr, k+1, temp)
            if temp:
                del used[temp.pop()]
        rec(nums)
        return ans

