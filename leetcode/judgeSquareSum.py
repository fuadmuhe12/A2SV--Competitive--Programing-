import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        start = 0
        end = int(sqrt(c))
        while start <= end:
            current_sum = start ** 2 + end ** 2
            if current_sum == c:
                return True
            elif current_sum >c:
                end -= 1
            else:
                start += 1
        return False
