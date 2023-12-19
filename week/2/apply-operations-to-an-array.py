class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        def movezero (lst):
            start = 0
            new = []
            ze = []
            while start < len(lst):
                if lst[start] != 0:
                    new.append(lst[start])
                else:
                    ze.append(lst[start])
                start += 1

            lst.clear()
            lst += new  + ze
            return lst
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                nums[i-1] *= 2
                nums[i] = 0
        return movezero (nums)
