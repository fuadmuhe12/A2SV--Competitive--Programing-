# Problem: Open the Lock - https://leetcode.com/problems/open-the-lock/

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        vis = set(deadends)
        if "0000" in vis:
            return -1

        que = deque([("0000", 0)])

        while que:
            cur, val = que.popleft()

            if cur == target:
                return val

            for i in range(4):
                for nexts in (-1, 1):
                    next_state = (
                        cur[:i]
                        + str((int(cur[i]) + nexts) % 10)
                        + cur[i + 1 :]
                    )
                    if next_state not in vis:
                        vis.add(next_state)
                        que.append((next_state, val + 1))

        return -1
