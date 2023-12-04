class Solution:
    def wateringPlants(self, plants: List[int], cap: int) -> int:
        tot = 0
        start = 0
        st = cap
        while start < len(plants):
            tot += 1
            cap -= plants[start]
            if start +1 < len(plants) and cap < plants[start +1]:
                tot += 2*(start + 1)
                cap = st
            start +=1 
        return tot
                
            