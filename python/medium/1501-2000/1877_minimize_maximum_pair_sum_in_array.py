from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums) // 2

        return max([x + y for x, y in zip(nums[: n + 1], nums[n:][::-1])])
