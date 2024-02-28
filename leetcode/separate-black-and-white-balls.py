class Solution:
    def minimumSteps(self, s: str) -> int:
        one = 0
        swap = 0
        for i in s:
            if  i == '1':
                one +=1
            else:
                swap += one

        return swap
