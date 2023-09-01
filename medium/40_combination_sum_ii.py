# https://leetcode.com/problems/combination-sum-ii/description/
from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        can = candidates
        n = len(candidates)
        def dfs(ans, curr, pos, remain):
            if remain == 0:
                ans += [list(curr)]
                return

            if pos == n:
                return

            for i in range(pos, n):
                if can[i] > remain:
                    break

                if i > pos and can[i] == can[i - 1]:
                    continue

                curr += [can[i]]
                dfs(ans, curr, i + 1, remain - can[i])
                curr.pop()
        ans = []
        dfs(ans, [], 0, target)
        return ans