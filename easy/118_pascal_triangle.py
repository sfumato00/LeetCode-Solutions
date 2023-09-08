from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            curr = [*ans[-1], 1] if ans else [1]
            for j in range(i - 1, 0, -1):
                curr[j] += curr[j - 1]
            ans += [curr]
        return ans
