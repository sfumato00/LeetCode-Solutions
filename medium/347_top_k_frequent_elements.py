from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        hp = []
        for key in cnt:
            heapq.heappush(hp, (cnt[key], key))
            if len(hp) > k:
                heapq.heappop(hp)
        return [k for _, k in hp]
