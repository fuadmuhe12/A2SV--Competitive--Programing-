class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sen = set()
        cur = 0
        flag = False
        ans = 0
        for ind, val in enumerate(arr):
            sen.add(val)
            flag= False
            cur =  max(val, cur, ind)
            for i in range(cur+1):
                if i not in sen:
                    break
            else:
                ans += 1
        return ans





