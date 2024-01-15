class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = []
        white = []
        blue = []
        for i in nums:
            if i == 0:
                red.append(i)
            elif i == 1:
                white.append(i)
            else:
                blue.append(i)
        nums[:] = red + white + blue