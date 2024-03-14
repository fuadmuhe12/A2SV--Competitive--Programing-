class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(left, right, cur = None):
            if right < left :
                return cur
            mid =  (right + left)//2
            if nums[mid] == target:
                cur  =  mid
                cur = findLeft(left, mid-1, cur )
                return cur
            if nums[mid] > target:
                cur = findLeft(left, mid-1, cur )
                return cur
            else:
                cur =  findLeft(mid +1, right, cur )
                return cur
        def find(left, right, cur = None):
            if right < left :
                return cur
            mid =  (right + left)//2
            if nums[mid] == target:
                cur  =  mid
                cur = find(mid +1, right, cur )
                return cur
            if nums[mid] > target:
                cur = find(left, mid-1, cur )
                return cur
            else:
                cur =  find(mid +1, right, cur )
                return cur
        left = findLeft(0, len(nums)-1)
        right = find(0, len(nums)-1)
        return [left if left != None else -1, right if right!= None else -1 ]
        
        