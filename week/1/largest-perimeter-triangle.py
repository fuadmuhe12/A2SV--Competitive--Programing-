class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse= True)
        per = 0
        end = 2
        start = 0
        while end < len(nums):
            a, b, c = nums[start:end+1]
            if a < b +c :
                per = a+ b+ c
                break
            else:
                start +=1 
                end += 1
        return per