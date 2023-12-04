class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if destination < start:
            start , destination = destination, start
        cur_sums = sum(distance[start:destination])
        tot_sums = sum(distance)
        if cur_sums < tot_sums-cur_sums:
            return cur_sums
        else:
            return tot_sums-cur_sums
        