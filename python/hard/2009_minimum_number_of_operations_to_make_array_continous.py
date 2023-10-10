from bisect import bisect_right
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        arr = sorted(set(nums))
        m = len(nums)
        ans = m
        for i, x in enumerate(arr):
            hi = x + m - 1
            j = bisect_right(arr, hi)
            ans = min(ans, m - j + i)
        return ans
