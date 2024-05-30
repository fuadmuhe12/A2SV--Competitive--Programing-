# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

import heapq
from collections import Counter


class MaxHeap:
    def __init__(self):
        self._queue = []
        
    def push(self, word, count):
        heapq.heappush(self._queue, (-count, word))
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]
        

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        
        heap = MaxHeap()
        
        for word, count in counter.items():
            heap.push(word, count)
            
        return [heap.pop() for _ in range(k)]