from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        for j, x in enumerate(nums):
            if x == 0:
                k -= 1
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
        return j - i + 1
