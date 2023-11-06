import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.n = len(w)
        self.pdf = [0] * self.n
        _sum = 0
        for i, x in enumerate(w):
            _sum += x
            self.pdf[i] = _sum

    def pickIndex(self) -> int:
        r = random.random()
        w = int(r * self.pdf[-1])
        # return bisect.bisect_right(self.pdf, w)
        lo, hi = 0, self.n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self.pdf[mid] <= w:
                lo = mid + 1
            else:
                hi = mid
        return lo


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
