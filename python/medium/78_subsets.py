class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans, curr = [], []
        n = len(nums)

        def dfs(pos):
            ans.append(list(curr))

            for i in range(pos, n):
                curr.append(nums[i])
                dfs(i + 1)
                curr.pop()

        dfs(0)
        return ans
