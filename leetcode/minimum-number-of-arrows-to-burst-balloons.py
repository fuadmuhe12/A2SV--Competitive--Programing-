class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        points.sort(key =  lambda point: point[0])
        cur =  float("-inf")
        for start, end in points :
            if start > cur:
                count += 1
                cur = end

            
            else:
                cur = min(cur, end)




        return count




