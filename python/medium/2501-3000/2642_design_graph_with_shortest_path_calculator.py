class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        self.n = n
        for e in edges:
            self.addEdge(e)

    def addEdge(self, edge: List[int]) -> None:
        u, v, c = edge
        self.graph[u] += [(v, c)]

    def shortestPath(self, node1: int, node2: int) -> int:
        dist = [inf] * self.n
        dist[node1] = 0
        hp = [(0, node1)]
        graph = self.graph
        while hp:
            d, u = heapq.heappop(hp)
            if u == node2:
                return dist[u]
            if d > dist[u]:
                continue
            for v, c in graph[u]:
                if (cost := dist[u] + c) < dist[v]:
                    dist[v] = cost
                    heapq.heappush(hp, (dist[v], v))
        return -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
