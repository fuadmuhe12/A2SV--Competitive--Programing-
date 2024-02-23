class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
      
        back = 0
        start = len(nums) - 1
        while start-1 >= 0:
            if nums[start-1] > nums[start]:
                sm = nums[start]
                big = nums[start-1]
                space = math.ceil(big/sm)                
                nums[start-1] = math.floor(big/space)
                back += space -1
           
            start -= 1
        return back

                