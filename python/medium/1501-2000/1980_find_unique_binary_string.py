from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        mem = set(nums)

        def build(curr):
            if len(curr) == n:
                if curr not in mem:
                    return curr
                return None

            return build(curr + "1") or build(curr + "0")

        return build("")


# class Solution:
#     def findDifferentBinaryString(self, nums: List[str]) -> str:

#         n = len(nums)

#         mem = {""}

#         for x in nums:
#             for i in range(1, n + 1):
#                 mem.add(x[:i])

#         def build(curr):
#             if curr not in mem:
#                 return curr + nums[0][len(curr):]

#             if len(curr) == n:
#                 return None

#             return build(curr + '1') or build(curr + '0')

#         return build("")
