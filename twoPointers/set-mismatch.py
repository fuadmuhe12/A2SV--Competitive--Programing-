class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        finds = defaultdict(int)
        
        ans = []
        for i in nums:
            finds[i] += 1
            if finds[i] >1:
                ans.append(i)
                break
        findss = set(nums)
        print(findss)
        for i in range(1, len(nums)+1):
            if i not in findss:
                ans.append(i)
                break
        return ans