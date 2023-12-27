class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = Counter(nums1)
        b= Counter(nums2)
        final = []
        for i in a:
            if i in b:
                final.extend([i]*min(a[i], b[i]))
        return final
        