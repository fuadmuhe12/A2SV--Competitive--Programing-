# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, root, k):
        parts = [None] * k

        count = 0
        cur = root
        while cur:
            count += 1
            cur = cur.next

        n, r = divmod(count, k)

        cur = root
        prev = None

        # Loop through each part.
        for i in range(k):
            parts[i] = cur

            for j in range(n + (1 if r > 0 else 0)):
                prev = cur
                cur = cur.next

            if prev:
                prev.next = None

            if r > 0:
                r -= 1

        return parts