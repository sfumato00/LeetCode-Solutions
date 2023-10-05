from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        out, stk = [0] * n, []

        for i, x in enumerate(heights):
            while stk and heights[stk[-1]] <= x:
                out[stk.pop()] += 1
            if stk:
                out[stk[-1]] += 1
            stk.append(i)
        return out
