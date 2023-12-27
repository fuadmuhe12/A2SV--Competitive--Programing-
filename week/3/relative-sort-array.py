class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mx = max(arr2)
        key = {}
        for ind , val in enumerate(arr2):
            key[val] = ind
        def adds(val):
            if val in key:
                return key[val]
            else:
                return val+ mx
        return sorted(arr1, key=adds)


