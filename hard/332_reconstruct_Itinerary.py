from collections import defaultdict
from typing import List
from sortedcontainers import SortedList

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        g = defaultdict(list)
        for u, v in tickets:
            g[u] += [v]

        for v in g.values():
            v.sort(reverse=True)

        ans = []

        def dfs(u):
            while g[u]:
                dfs(g[u].pop())
            ans.append(u)

        dfs("JFK")
        return ans[::-1]
