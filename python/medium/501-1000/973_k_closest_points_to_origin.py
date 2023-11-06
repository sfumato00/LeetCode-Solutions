import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            heapq.heappush(maxHeap, (-(x**2 + y**2), [x, y]))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [x[1] for x in maxHeap]
