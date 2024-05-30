# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for val in range(len(triangle)-2,-1,-1) :  
            for col in range(len(triangle[val])) :
                triangle[val][col] += min(triangle[val+1][col] , triangle[val+1][col+1])
        return (triangle[0][0])
        if not triangle :
            return 0