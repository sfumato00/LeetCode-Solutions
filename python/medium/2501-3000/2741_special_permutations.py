from collections import defaultdict
from typing import List


class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        MOD = 1_000_000_007

        g = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                x, y = nums[i], nums[j]
                if x % y == 0 or y % x == 0:
                    g[i] += [j]
                    g[j] += [i]
        g[-1] = list(range(n))
        target = (1 << n) - 1

        @cache
        def dfs(u, state):
            if state == target: return 1

            count = 0
            for v in g[u]:
                if state & (mask := 1 << v):
                    continue

                count += dfs(v, state | mask)
                count %= MOD
            return count
        
        return dfs(-1, 0)
