from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)

        if n < 2:
            return n

        nums.sort()
        max_freq, l = 1, 0

        for r, x in enumerate(nums[1:], start=1):
            extra_ops = (x - nums[r - 1]) * (r - l)

            while k < extra_ops:
                extra_ops -= x - nums[l]
                l += 1

            k -= extra_ops
            max_freq = max(max_freq, r - l + 1)

        return max_freq
