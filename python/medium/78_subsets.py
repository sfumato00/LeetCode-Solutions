from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, curr = [], []

        def dfs(pos):
            if pos == n:
                ans.append(list(curr))
                return

            dfs(pos + 1)
            curr.append(nums[pos])
            dfs(pos + 1)
            curr.pop()

        dfs(0)
        return ans
