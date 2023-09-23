from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        lm, rm = 0, 0
        ans = 0
        while lo <= hi:
            lm = max(lm, height[lo])
            rm = max(rm, height[hi])

            if lm <= rm:
                ans += lm - height[lo]
                lo += 1
            else:
                ans += rm - height[hi]
                hi -= 1
        return ans
