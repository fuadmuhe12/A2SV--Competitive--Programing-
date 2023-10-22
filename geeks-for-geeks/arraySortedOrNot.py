class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        start = 0
        end  = 1
        while end < n:
            if arr[start] > arr[end]:
                return 0
            start += 1
            end += 1
        return 1
