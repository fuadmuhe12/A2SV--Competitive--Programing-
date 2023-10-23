class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        start = 0
        end = 0
        answer = []
        while end <len(nums):
            if nums[end] == target:
                while end <len(nums) and nums[end] == target:
                    answer.append(end)
                    end += 1
                break
            end += 1
        return answer
            
