from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if not nums or (n := len(nums)) <= 1:
            return 0

        far = bound = steps = 0
        for i, x in enumerate(nums):
            if (y := i + x) > far:
                far = y

            if far >= n - 1:
                return steps + 1

            if i == bound:
                steps += 1
                bound = far

        return -1
