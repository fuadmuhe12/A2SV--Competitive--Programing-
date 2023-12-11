class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n =  len(arr)//4
        dic =Counter(arr)
        for key, val in dic.items():
            if val > n:
                return key