class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stk, out = [], [-1] * n
        for _ in range(2):
            for i in range(n):
                while stk and nums[stk[-1]] < nums[i]:
                    out[stk.pop()] = nums[i]
                stk.append(i)
        return out
