class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if right >> 1 >= left:
            return 0
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
