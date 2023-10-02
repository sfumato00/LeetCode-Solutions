from collections import deque
from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            bal = 0
            for _, ch in enumerate(s):
                if ch == "(":
                    bal += 1
                elif ch == ")":
                    bal -= 1
                    if bal < 0:
                        return False
            return bal == 0

        q = deque([s])
        seen = set([s])
        out = []
        while q and not out:
            level_n = len(q)
            for _ in range(level_n):
                curr = q.popleft()

                if is_valid(curr):
                    out += [curr]

                if not out:
                    for i, ch in enumerate(curr):
                        if ch != "(" and ch != ")":
                            continue

                        _next = curr[:i] + curr[i + 1 :]
                        if _next not in seen:
                            q += [_next]
                            seen.add(_next)
        return out
