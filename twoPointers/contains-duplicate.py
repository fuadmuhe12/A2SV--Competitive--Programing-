class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
            if count[i] >1:
                return True
        else:
            return False
