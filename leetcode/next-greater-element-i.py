class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        stack = []
        for i in nums2:
            if not stack:
                stack.append(i)
                dic[i] = -1
            else:
                while stack  and  i > stack[-1]:
                    dic[stack[-1]] =  i
                    stack.pop()
                        
                dic[i] = -1
                stack.append(i)
        ans = []
        for i in nums1:
            ans.append(dic[i])
        return ans
                    

