"""1814. Count Nice Pairs in an Array"""
from collections import defaultdict
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            return int(str(x)[::-1])

        MOD = 10**9 + 7
        mem = defaultdict(int)
        for x in nums:
            y = rev(x)
            k = x - y
            mem[k] += 1
            mem[k] %= MOD

        ans = 0
        for cnt in mem.values():
            ans += (cnt * (cnt - 1)) // 2
            ans %= MOD

        return ans
