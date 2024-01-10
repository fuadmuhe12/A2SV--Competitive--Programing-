class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        v = set(nums1).intersection(set(nums2)) 
        if  v != set() :
            return min(v)
        else:
            return  -1