import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(a, b):
            return abs(points[a][0] - points[b][0]) + abs(points[a][1] - points[b][1])

        def find(x):
            p = parent[x]
            while p != parent[p]:
                parent[p], p = parent[parent[p]], parent[p]
            return p

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[py] > rank[px]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        n = len(points)
        hp = []
        for i in range(n):
            for j in range(i + 1, n):
                heapq.heappush(hp, (manhattan(i, j), i, j))

        parent = list(range(n))
        rank = [1] * n

        ans = 0
        count = 0
        while count < n - 1:
            m, x, y = heapq.heappop(hp)
            is_unioned = union(x, y)
            count += 1 if is_unioned else 0
            ans += m if is_unioned else 0

        return ans
