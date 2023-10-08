from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        _min1, _max1 = min(nums1), max(nums1)
        _min2, _max2 = min(nums2), max(nums2)

        if _max1 < 0 and _min2 > 0:
            return _max1 * _min2

        if _max2 < 0 and _min1 > 0:
            return _max2 * _min1

        m, n = len(nums1), len(nums2)

        # @cache
        # def dp(i, j):

        #     if i == m or j == n:
        #         return 0

        #     return max(nums1[i] * nums2[j] + dp(i + 1, j + 1), dp(i, j + 1), dp(i + 1, j))

        # return dp(0, 0)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(
                    nums1[i - 1] * nums2[j - 1] + dp[i - 1][j - 1],
                    dp[i - 1][j],
                    dp[i][j - 1],
                )
        return dp[m][n]
