from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        def solution1():
            total_profit, profit = 0, 0
            cost = inf
            for i in range(n):
                if prices[i] - cost < profit:
                    total_profit += profit
                    profit = 0
                    cost = prices[i]
                else:
                    profit = prices[i] - cost
                    cost = min(cost, prices[i])
            return total_profit + profit

        def solution2():
            return sum(
                [
                    prices[i] - prices[i - 1]
                    for i in range(1, n)
                    if prices[i] > prices[i - 1]
                ]
            )

        return solution2()
