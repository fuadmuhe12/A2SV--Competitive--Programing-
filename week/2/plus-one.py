class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = "".join(map(str, digits))
        n += " + 1"
        n = str(eval (n))


       
        return list(map(int, n ))