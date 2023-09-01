from typing import *

# https://leetcode.com/problems/subsets-ii/description/
class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []

        def dfs(n, pos, curr):
            nonlocal ans
            ans += [list(curr)]
            for i in range(pos, n):
                if i > pos and nums[i] == nums[i - 1]:
                    continue
                curr += [nums[i]]
                dfs(n, i + 1, curr)
                curr.pop()

        n = len(nums)
        dfs(n, 0, [])
        return ans