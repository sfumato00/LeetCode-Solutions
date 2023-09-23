from math import inf
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        mat, mde = -inf, -inf
        for at, de in properties:
            if at < mat and de < mde:
                ans += 1
            else:
                mat, mde = at, de
        return ans
