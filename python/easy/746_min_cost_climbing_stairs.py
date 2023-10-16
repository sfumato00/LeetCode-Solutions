from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2, prev1 = cost[0], cost[1]
        for x in cost[2:]:
            temp = min(prev2, prev1) + x
            prev2, prev1 = prev1, temp
        return min(prev2, prev1)
