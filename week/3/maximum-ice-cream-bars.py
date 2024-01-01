class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counting = [0]*(max(costs)+1)
        for i in costs:
            counting[i] += 1
        ind = 0
        count = 0
        while ind < len(counting) and coins-(ind) >=0:
            while coins -ind >= 0 and counting[ind] > 0:
                coins -= ind
                counting[ind] -= 1
                count += 1
            ind += 1
        return count



