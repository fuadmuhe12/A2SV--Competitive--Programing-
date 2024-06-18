# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    
    def mostPoints(self, questions: List[List[int]]) -> int:
        len_ = len(questions)
        memo = [0] * len_
        memo[len_ - 1] = questions[len_ - 1][0]
        for i in range(len_ - 2, -1, -1):
            nexSco = memo[i + 1]
            curscor = (
                questions[i][0] + memo[i + questions[i][1] + 1]
                if i + questions[i][1] + 1 < len_
                else questions[i][0]
            )
            memo[i] = max(nexSco, curscor)

        return memo[0]
