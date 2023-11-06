from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        stk = []

        for i, c in enumerate(colors):
            if not stk or colors[stk[-1]] != c:
                stk.append(i)
            elif neededTime[stk[-1]] < neededTime[i]:
                stk[-1] = i

        return sum(neededTime) - sum([neededTime[x] for x in stk])
