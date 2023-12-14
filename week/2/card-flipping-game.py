class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        """

        1. similar = if vak of back and frott of one are == , all of them should be at back  put all of them below   
        2. if num is unique(), it should be at the top
        3 .see frequency of value if value not in similar put one on top and other below, 
        4. below 1st for similar , 2nd for frequency whcih
        
        """
        similar = {fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i] }
        back =set(backs + fronts)

        mn = float('inf')
        for i in  back:
            if i not in similar:
                mn = min(mn, i)

        return mn if mn != float('inf') else 0

