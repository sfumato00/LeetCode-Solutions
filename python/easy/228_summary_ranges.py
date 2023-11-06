from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n, start = len(nums), 0
        output = []
        for end, x in enumerate(nums):
            if end == n - 1 or nums[end + 1] > x + 1:
                output += (
                    [str(nums[start]) + "->" + str(x)] if end > start else [str(x)]
                )
                start = end + 1

        return output
