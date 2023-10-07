from functools import cache
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @cache
        def dfs(l, r):
            if l > r:
                return 0

            ret = 0
            for i in range(l, r + 1):
                ret = max(
                    ret,
                    nums[l - 1] * nums[i] * nums[r + 1] + dfs(l, i - 1) + dfs(i + 1, r),
                )
            return ret

        return dfs(1, len(nums) - 2)
