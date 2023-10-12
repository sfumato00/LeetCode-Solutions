from functools import cache


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        @cache
        def search(pos, target):
            if pos == n:
                return 1 if target == 0 else 0
            return search(pos + 1, target - nums[pos]) + search(pos + 1, target + nums[pos])
        return search(0, target)