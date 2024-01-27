class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # recurcive with base case of finding A two values that satisfy the case 
        # nums = [1,0,-1,0,-2,2]
        # target = 0
        nums.sort()
        ans = set()
        quad = []
        def solve(start, k , target ):
            if k != 2:
                for i in range(start, len(nums) -k+1 ):
                    if i > start and nums[i] ==  nums[i-1]: continue
                    quad.append(nums[i])
                    start = i+1
                    solve(start, k-1, target -nums[i])
                    quad.pop()
                    

            else:
                l = start

                r = len(nums)-1
                while r > l:
                    if nums[l] + nums[r] > target: 
                        r -= 1
                    elif nums[l] + nums[r] < target:
                        l += 1
                    else:
                        quad.extend([nums[l], nums[r]])
                        ans.add(tuple(quad[:]))
                        quad.pop()
                        quad.pop()
                        while l < r :
                            if nums[l] == nums[l+1]:
                                l += 1
                            else:
                                l += 1
                                break
                        
        solve(0, 4, target)
        return [list(i) for i in ans]
                    


               
