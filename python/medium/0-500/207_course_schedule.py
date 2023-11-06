from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        graph = [[] for _ in range(n)]
        for v, u in prerequisites:
            graph[u] += [v]

        stk = [False] * n
        cache = {}

        def dfs(u):
            if u in cache:
                return cache[u]

            stk[u] = True
            for v in graph[u]:
                if stk[v] or not dfs(v):
                    cache[u] = False
                    return False
            stk[u] = False
            cache[u] = True
            return True

        for u in range(n):
            if not dfs(u):
                return False
        return True
