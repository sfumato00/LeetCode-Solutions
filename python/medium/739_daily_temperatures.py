from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = []
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            while stk and temperatures[i] >= temperatures[stk[-1]]:
                stk.pop()
            if stk:
                ans[i] = stk[-1] - i
            stk += [i]
        return ans
