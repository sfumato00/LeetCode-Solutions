from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, curr = [], []
        visited = [False] * n

        def dfs(pos):
            if pos == n:
                ans.append(list(curr))
                return
            for i, x in enumerate(nums):
                if visited[i]:
                    continue
                visited[i] = True
                curr.append(x)
                dfs(pos + 1)
                curr.pop()
                visited[i] = False

        dfs(0)
        return ans
