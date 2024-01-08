class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = []
        n = nums.count(val)
        for i in nums:
            if i != val:
                ans.append(i)
        for i in range(len(ans)):
            nums [i] == ans[i]
        nums[:] = ans[:]
        print(ans)
       
        return len(ans)

        