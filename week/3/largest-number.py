class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def x_isgreat_y(x, y):
            return    x+y > y+x
        nums =list(map(str, nums))

        for i in range(len(nums)):
            swap = False
            for i in range(1, len(nums)):
                if  x_isgreat_y(nums[i], nums[i-1]) :
                    nums[i], nums[i-1] = nums[i-1],nums[i]
                    swap = True
            if not swap:
                break
        x= ''.join(nums)
        if x[0] == '0':
            return "0"
        else:
            return x


        






