import collections
import heapq
from typing import List


class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        adj = collections.defaultdict(list)
        for i, (u, v) in enumerate(edges):
            adj[u] += [(v, succProb[i])]
            adj[v] += [(u, succProb[i])]
        seen = set()
        hp = [(-1, start_node)]
        while hp:
            prop, u = heapq.heappop(hp)
            if u == end_node:
                return -prop
            if u in seen:
                continue
            seen.add(u)
            for v, p in adj[u]:
                heapq.heappush(hp, (prop * p, v))
        return 0
