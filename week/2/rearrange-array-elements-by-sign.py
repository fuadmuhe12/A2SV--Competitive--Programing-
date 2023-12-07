class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [i for i in nums if i > 0]
        nev = [i for i in  nums if i < 0]
        ans = []
        for i in range(len(nums)//2):
            ans.append(pos[i])
            ans.append(nev[i])
        return ans
