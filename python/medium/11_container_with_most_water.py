from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        ans = 0
        while lo < hi:
            ans = max(ans, (hi - lo) * min(height[lo], height[hi]))
            if height[lo] <= height[hi]:
                lo += 1
            else:
                hi -= 1
        return ans
