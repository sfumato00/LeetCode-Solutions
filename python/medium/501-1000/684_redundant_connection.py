from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            while parents[x] != x:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        n = len(edges)
        parents = [x for x in range(n + 1)]  # vertices index starts with 1
        for u, v in edges:
            p_u = find(u)
            p_v = find(v)
            if p_u == p_v:
                return [u, v]
            parents[p_u] = p_v
        return []
