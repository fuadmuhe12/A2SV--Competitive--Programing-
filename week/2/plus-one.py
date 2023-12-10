class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = "".join(map(str, digits))
        n = str(int(n)+1)
        n = list(n)
        for i in range(len(n)):
            n[i] = int(n[i])
        return n