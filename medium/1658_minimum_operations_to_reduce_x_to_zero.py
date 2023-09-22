from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # Transform the problem to "Find the longest Sub-array where the sum is equal to target"
        n, target = len(nums), sum(nums) - x
        if target == 0:
            return n
        lo = 0
        max_len, _sum = -1, 0
        for hi, val in enumerate(nums):
            _sum += val
            while lo < hi and _sum > target:
                _sum -= nums[lo]
                lo += 1
            if _sum == target:
                max_len = max(max_len, hi - lo + 1)
        return -1 if max_len == -1 else n - max_len
