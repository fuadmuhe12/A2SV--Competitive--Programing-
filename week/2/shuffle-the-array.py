class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        pointer_1 = 0
        pointer_2 = n
        result = []
        while pointer_2 < len(nums):
            result.extend([nums[pointer_1], nums[pointer_2]])
            pointer_1 += 1
            pointer_2 += 1
        return result 
