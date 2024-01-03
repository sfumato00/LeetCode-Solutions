from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stk = [-1]
        n = len(heights)
        ans = 0
        for i in range(n):
            while stk[-1] != -1 and heights[stk[-1]] > heights[i]:
                h = heights[stk.pop()]
                w = i - stk[-1] - 1
                ans = max(ans, h * w)
            stk += [i]

        while stk[-1] != -1:
            h = heights[stk.pop()]
            w = n - stk[-1] - 1
            ans = max(ans, h * w)

        return ans 