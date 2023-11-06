from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans, curr = [], []

        def dfs(pos):
            ans.append(list(curr))
            for i in range(pos, n):
                if i > pos and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                dfs(i + 1)
                curr.pop()

        dfs(0)
        return ans
