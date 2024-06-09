# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        

        trie = {}
        def add(n):
            node = trie
            for i in range(31, -1, -1):
                val = 1 if  (n >> i) & 1 > 0 else 0
                
                node = node.setdefault(val, {})
        
        for n in nums:
            add(n)
        
        def sums(n):
            node = trie
            s = 0
            for i in range(31, -1, -1):
                val = 1 if  (n >> i) & 1 > 0 else 0
                if 1 - val in node:
                    s += 1 << i
                    node = node[1-val]
                else:
                     node = node[val]
            return s
        ans = 0
        for n in nums:
            ans = max(ans, sums(n))
        return ans