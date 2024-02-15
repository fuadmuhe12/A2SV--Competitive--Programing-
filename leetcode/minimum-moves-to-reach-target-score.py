class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        # when to doule 
        arr = []
        cur = target
        
        for i in range(maxDoubles):
            if cur == 1:
                break
            cur = cur//2
            
            arr.append(cur)
        cur = 1
        ans = 0
        for i in range(len(arr)-1, -1, -1):
            ans += arr[i] - cur +1 
            cur = arr[i]*2
        return ans + target - cur



        