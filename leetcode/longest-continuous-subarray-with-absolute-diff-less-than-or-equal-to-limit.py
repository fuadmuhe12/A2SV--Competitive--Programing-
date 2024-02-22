class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        que  =  deque()
        de = deque()
        stack = []
        start = 0
        end = 0
        mx = 0
        for ind, val in enumerate(nums):
            while que and que[-1] > val:
                que.pop()
            que.append(val)
            while de  and de[-1] < val:
                de.pop()
            de.append(val)
            dif = abs(de[0] - que[0])
            while dif > limit:
                if nums[start] == de[0]:
                    de.popleft()
                if nums[start] ==  que[0]:
                    que.popleft()
                start += 1
                dif = abs(de[0] - que[0])
            mx = max(mx, ind - start +1)
        return mx

            





                      

