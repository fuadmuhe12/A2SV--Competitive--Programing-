class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 1:
            return duration 
        else:
            tot = 0
            for i in range(1, len(timeSeries)):
                tot +=  min((timeSeries[i] - timeSeries[i-1]), duration )
            tot += duration 
            return tot