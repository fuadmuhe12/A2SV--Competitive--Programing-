class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for i in range(left, right+1):
            for x, y in ranges:
                if x <= i <= y:
                    break
            else:
                return False
        return True

