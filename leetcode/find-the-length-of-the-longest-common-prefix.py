class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        ar1 = set()
        for i in set(arr1):
            val =  str(i)
            for i in range(len(val)):
                ar1.add(val[:i+1])
        mx = 0
        for i in set(arr2):
            val =  str(i)
            for i in range(len(val)):
                if val[:i+1] in ar1:
                    mx = max(mx, i +1)
        return mx


