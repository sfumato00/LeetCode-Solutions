from math import inf
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans, diff = None, inf
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                _sum = nums[i] + nums[l] + nums[r]
                _diff = abs(_sum - target)
                if _diff == 0:
                    return _sum

                if abs(_sum - target) < diff:
                    ans = _sum
                    diff = _diff

                if _sum < target:
                    l += 1
                else:
                    r -= 1
        return ans
