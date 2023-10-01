from math import inf
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        third, stk = -inf, []
        for x in nums[::-1]:
            if x < third:
                return True
            while stk and stk[-1] < x:
                third = stk.pop()
            stk += [x]

        return False
