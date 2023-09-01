import heapq
from typing import List


def use_heap(points: List[List[int]], k: int) -> List[List[int]]:
    hp = [(p[0] ** 2 + p[1] ** 2, i) for i, p in enumerate(points)]
    heapq.heapify(hp)
    return [points[heapq.heappop(hp)[1]] for _ in range(k)]


def use_sort(points: List[List[int]], k: int) -> List[List[int]]:
    return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:k]


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # return use_heap(points, k)
        return use_sort(points, k)
