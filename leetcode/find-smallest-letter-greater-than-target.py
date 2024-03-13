class Solution:
    def nextGreatestLetter(self, let: List[str], tar: str) -> str:
        def find(left, right, cur = None):
            if left > right:
                return cur
            mid  =  (left + right)//2
            if let[mid] > tar:
                cur =  let[mid]
                cur = find(left, mid -1, cur)
            else:
                cur = find(mid +1, right, cur)
            return cur
        return find(0, len(let)-1) if  find(0, len(let)-1) else let[0]
        

