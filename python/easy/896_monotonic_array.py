from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc, dec = True, True
        for x, y in zip(nums[:-1], nums[1:]):
            inc &= x <= y
            dec &= x >= y
        return inc or dec
