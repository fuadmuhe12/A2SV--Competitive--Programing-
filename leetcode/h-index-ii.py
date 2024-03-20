class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 1
        high = len(citations)
        cur = 0
        while low <= high:
            mid = (low + high)//2

            ind = len(citations) - mid
            
            if citations[ind] >= mid:
                low = mid + 1
                cur = mid
            else:
                high = mid - 1
        return cur
        