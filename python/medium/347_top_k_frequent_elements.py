from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        return sorted(list(cnt.keys()), key=lambda x: -cnt[x])[:k]
