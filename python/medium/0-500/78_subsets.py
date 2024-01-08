from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        # BFS
        for x in nums:
            temp = []
            for cur in ans:
                temp += [cur + [x]]
            ans += temp
        return ans

        # pythonic
        # for x in nums:
        #     ans += [cur + [x] for cur in ans]
        # return ans
