class Solution:
    def isPalindrome(self, s: str) -> bool:
        var = [i.lower() for i in s if i.isalnum()]
        def fin(lst, start, end):
            if len(lst) <= 1:
                return True
            elif lst[start] != lst[end]:
                return False
            elif start == end:
                return True
            elif start > end:
                return True
            else:
                return fin(lst, start + 1, end - 1)

        return fin(var, 0, len(var )- 1)
