class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        mx = max(trips, key= lambda a: a[2])[2]
        acc = 0
        arr = [0] * (mx+1)
        for cap, start , end in trips:
            arr[start] += cap
            arr[end] -= cap
        run = 0
        for ind , val in enumerate(arr):
            run += val
            if run > capacity:
                return False
        return True

            

        