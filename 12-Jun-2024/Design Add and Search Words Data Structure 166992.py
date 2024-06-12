# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        val = self.root
        for curword in word:
            if curword not in val.children:
                val.children[curword] = TrieNode()
            val = val.children[curword]  
        val.is_word = True    

    def search(self, word: str) -> bool:
        stack = [(self.root,0)]
        while stack:
            val,i = stack.pop()
            if i == len(word):
                if val.is_word:
                    return True
            elif word[i] == '.':
                for child in val.children.values():
                    stack.append((child,i+1))
            elif word[i] in val.children:
                stack.append((val.children[word[i]], i+1))
        return False
        