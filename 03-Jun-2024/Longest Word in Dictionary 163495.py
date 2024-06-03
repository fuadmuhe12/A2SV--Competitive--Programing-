# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()

        for wo in words:
            cur = root
            for letter in wo:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode()
                cur = cur.children[letter]
            cur.end = True
            
        res = ''
        
        for wo in words:
            if len(wo) < len(res): continue
            
            cur = root
            
            for letter in wo:
                cur = cur.children[letter]
                if not cur.end: break
            
            if cur.end and (len(wo) > len(res) or (len(wo) == len(res) and wo < res)):
                res = wo        
            
        return res