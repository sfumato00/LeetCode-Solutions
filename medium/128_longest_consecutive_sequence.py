from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        pool = set(nums)
        ans = 0
        for x in pool:
            if x - 1 not in pool:
                y = x
                while y + 1 in pool:
                    y += 1
                ans = max(ans, y - x + 1)
        return ans
