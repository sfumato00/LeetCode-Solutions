from collections import defaultdict, deque
from math import inf
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time = [inf] * (n + 1)
        time[k] = 0
        g = defaultdict(list)
        for u, v, w in times:
            g[u] += [(v, w)]

        q = deque([k])
        cnt = 0
        while q:
            u = q.popleft()
            cnt += 1
            for v, w in g[u]:
                if time[u] + w < time[v]:
                    time[v] = time[u] + w
                    q += [v]
        return -1 if cnt < n else max(time[1:])
