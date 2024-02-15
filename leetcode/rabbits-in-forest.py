class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        num = Counter(answers)
        zer =  answers.count(0)
        for i in num.keys():
            if i ==  0:
                continue
            ans += (i + 1)*(math.ceil(num[i]/(i+ 1)))
        return ans + zer


