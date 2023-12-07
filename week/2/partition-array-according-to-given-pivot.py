class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        middle = []
        end = []
        ans = []
        for i in nums:
            if i > pivot:
                end.append(i)
            elif i < pivot:
                ans.append(i)
            else:
                middle.append(i)
        return ans + middle + end