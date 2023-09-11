from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # return use_dfs(nums, target)
        return use_dp(nums, target)


def use_dp(nums: List[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1

    for i in range(target + 1):
        for x in nums:
            if i + x <= target:
                dp[i + x] += dp[i]
    return dp[target]


def use_dfs(nums: List[int], target: int) -> int:
    cache = {}

    def dfs(rem):
        if rem == 0:
            return 1
        if rem in cache:
            return cache[rem]

        ret = 0
        for x in nums:
            if rem >= x:
                ret += dfs(rem - x)
        cache[rem] = ret
        return ret

    return dfs(target)
