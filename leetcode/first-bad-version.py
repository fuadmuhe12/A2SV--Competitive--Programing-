# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        def find(left, right, cur = None):
            if right < left :
                return cur
            mid =  (right + left)//2
            if isBadVersion(mid):
                cur  =  mid
                cur = find(left, mid-1, cur )
                return cur
            else:
                cur = find(mid+1, right, cur )
                return cur
        return find(1, n)
