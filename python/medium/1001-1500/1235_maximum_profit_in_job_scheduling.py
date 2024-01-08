from bisect import bisect_left
from typing import List


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        tasks = sorted(zip(endTime, startTime, profit))
        dp = [0]
        end_time = [0]

        for e, s, p in tasks:
            i = bisect_left(end_time, s + 1) - 1
            if dp[i] + p > dp[-1]:
                dp += [dp[i] + p]
                end_time += [e]

        return dp[-1]
