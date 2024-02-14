class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        A =  [a - b for a, b in costs]
        mush = [[A[i],  costs[i]] for i in range(len(costs))]
        mush.sort(key = lambda a: a[0])
        print(mush)
        ans  = 0
        for i in range(len(mush)):
            if i < len(costs)//2:
                ans += (mush[i][1][0])
            else:
                ans += (mush[i][1][1])
        return ans

        
