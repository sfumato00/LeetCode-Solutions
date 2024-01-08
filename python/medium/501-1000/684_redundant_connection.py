from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        # parents = {x: x for x in range(1, n + 1)}
        parents = [x for x in range(n + 1)]
        rank = [1] * (n +  1)

        def find(x):
            while parents[x] != x:
                parents[x], x = parents[parents[x]], parents[x]
            return x

        for u, v in edges:
            p_u, p_v = find(u), find(v)
            if p_u == p_v:
                return [u, v]
            if rank[p_v] > rank[p_u]:
                p_u, p_v = p_v, p_u
            parents[p_v] = p_u
            if rank[p_v] == rank[p_u]:
                rank[p_u] += 1
        return []
