class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        cur = float('inf')
        dic_ind = {}
        for ind, val in enumerate(cards):
            if val in dic_ind:
                cur = min((ind - dic_ind[val] +1), cur)
                dic_ind[val] = ind
            else:
                dic_ind[val ] = ind
        return cur if cur != float('inf') else -1