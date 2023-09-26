from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # lo, hi = 1, max(piles)
        s = sum(piles)
        lo = ceil(s / h)
        hi = ceil(s / (h - len(piles) + 1))
        ans = -1
        while lo <= hi:
            k = lo + (hi - lo) // 2
            hr = 0
            for i, x in enumerate(piles):
                hr += ceil(x / k)
            if hr <= h:
                ans = k
                hi = k - 1
            else:
                lo = k + 1
        return ans
