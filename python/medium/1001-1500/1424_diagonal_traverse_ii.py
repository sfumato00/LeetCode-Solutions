from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        memo = defaultdict(list)

        for i, row in enumerate(nums):
            for j, x in enumerate(row):
                memo[i + j].append(x)

        out = []
        i = 0
        while i in memo:
            out += memo[i][::-1]
            i += 1
        return out
