# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None for i in range(26)]

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if not cur.children[ord(char) - ord('a')]:
                new_trie = TrieNode()
                cur.children[ord(char) - ord('a')] = new_trie
                cur = new_trie
            else:
                cur = cur.children[ord(char) - ord('a')]
        cur.is_end = True
    def search(self, word: str) -> str:
        cur = self.root
        temp = ''

        for char in word:
            if not cur.children[ord(char) - ord('a')]:
                return temp if cur.is_end else ''
            else:
                if cur.is_end:
                    return temp
                temp+=char
                cur = cur.children[ord(char) - ord('a')]
        return temp  if cur.is_end else ''



class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        my_trie_ = Trie()
        for i in  dictionary:
            my_trie_.insert(i)
        sen = sentence.split()

        for i in range(len(sen)):
            store  = my_trie_.search(sen[i])
            if store!='':
                sen[i] = store
        return ' '.join(sen)