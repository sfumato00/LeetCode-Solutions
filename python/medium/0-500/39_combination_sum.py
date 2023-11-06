from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sorted_candidates = sorted(candidates)
        ans, curr = [], []
        length = len(sorted_candidates)

        def dfs(pos, remain):
            if remain == 0:
                ans.append(list(curr))
                return

            while pos < length and sorted_candidates[pos] <= remain:
                curr.append(sorted_candidates[pos])
                dfs(pos, remain - sorted_candidates[pos])
                curr.pop()
                pos += 1

        dfs(0, target)
        return ans
