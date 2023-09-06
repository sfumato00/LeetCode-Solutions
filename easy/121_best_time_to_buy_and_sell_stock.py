from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        lowest = inf
        for x in prices:
            ans = max(ans, x - lowest)
            lowest = min(lowest, x)
        return ans
