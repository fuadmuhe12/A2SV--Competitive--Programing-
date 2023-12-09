class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        ans = []
        for i in range(len(boxes)):
            sums = 0
            for j in range(len(boxes)):
                if int(boxes[j]) == 1:
                    sums += abs(j-i)
            ans.append(sums)
           
        return ans
                