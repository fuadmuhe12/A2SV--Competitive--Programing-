class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        low = 0 
        high = max(houses[-1], heaters[-1])
        ans = high
        while high >= low:
            mid = (high + low)//2
            pot = 0

            for i in heaters:
                start = i-mid
                end = i + mid
                if pot >= len(houses):
                    break
                while start <= houses[pot] <= end:
                    pot += 1
                    if pot >= len(houses):
                        break
                
            if pot >= len(houses):
                ans = mid
                high = mid -1
            else:
                low = mid + 1
        return ans


