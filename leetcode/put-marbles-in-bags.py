class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        weSum = []
        for x, y in (zip(weights, weights[1:])):
            weSum.append(x+y)
        maxSum = weights[0] + weights[-1]
        minSum = weights[0] + weights[-1]
        weSum.sort()

        for s in range(k-1):
            maxSum += weSum[len(weSum) - s-1]
            minSum += weSum[s] 
        return maxSum - minSum


        

