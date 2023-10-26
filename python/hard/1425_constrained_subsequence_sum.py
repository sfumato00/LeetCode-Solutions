from typing import Deque, List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n, q = len(nums), Deque()
        dp = [0] * n

        for i, x in enumerate(nums):
            if q and i - q[0] > k:
                q.popleft()

            dp[i] = (dp[q[0]] if q else 0) + x

            while q and dp[i] >= dp[q[-1]]:
                q.pop()

            if dp[i] > 0:
                q.append(i)

        return max(dp)
