class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        mx = max(arr)
        cur = arr[0]
        if len(arr) <3 or arr[0]== mx or arr[-1] == mx:
            return False
        else:
            mx_reached = False
            for i in range(1, len(arr)):
                if arr[i] == mx:
                    mx_reached =True
                    cur = mx
                    continue
                if mx_reached:
                    if arr[i] >= cur:
                        return False
                    cur = arr[i]
                if not mx_reached:
                     
                    if arr[i] <= cur:
                        return False
                    cur = arr[i]
            return True
        