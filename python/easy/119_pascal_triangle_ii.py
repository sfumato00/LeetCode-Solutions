class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1]
        for i in range(rowIndex):
            for j in range(i, 0, -1):
                dp[j] += dp[j - 1]
            dp += [1]
        return dp
