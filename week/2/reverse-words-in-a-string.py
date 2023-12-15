class Solution:
    def reverseWords(self, s: str) -> str:
        m = list(s.split())[::-1]
        a = len(m)
        b = 0
        answer = ""
        while b < a:
            if b+1 < a:
                answer += m[b] + " "
            elif b+1 >= a:
                answer += m[b]
            b += 1
        return answer

        