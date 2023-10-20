class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        g = defaultdict(list)
        indegree = [0] * n
        # O(E)
        for u, v in relations:
            g[u] += [v]
            indegree[v - 1] += 1

        # O(V)
        q = deque()
        dist = [0] * n
        for v in range(n):
            if indegree[v] == 0:
                q += [v + 1]
                dist[v] = time[v]

        # O(V + E)
        while q:
            u = q.popleft()
            for v in g[u]:
                indegree[v - 1] -= 1
                if dist[u - 1] + time[v - 1] > dist[v - 1]:
                    dist[v - 1] = dist[u - 1] + time[v - 1]
                if indegree[v - 1] == 0:
                    q += [v]
        return max(dist)
