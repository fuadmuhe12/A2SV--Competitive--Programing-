class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import defaultdict
        sums = 0
        x = defaultdict(int)
        for i in nums:
            x[i] += 1
        for i in x.values():
            if i == 1:
                pass
            else:
                sums += i*(i+1)//2 -i
        return sums
