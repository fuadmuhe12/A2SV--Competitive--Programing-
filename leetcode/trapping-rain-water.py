class Solution:
    def trap(self, height: List[int]) -> int:
        rm = 0
        rlis = []
        oplis = deque()
        opm = 0
        for i in height:
            rlis.append(max(rm, i))
            rm =  max(rm, i)
        for i in range(len(height)-1, -1, -1):
            oplis.appendleft(max(opm, height[i]))
            opm =  max(opm, height[i])
        ans = 0
        for ind, val in enumerate(height):
            ans += min(oplis[ind], rlis[ind]) - val
        return ans


