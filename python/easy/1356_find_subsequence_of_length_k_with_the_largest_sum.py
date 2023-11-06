from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_ones(num):
            count = 0
            while num > 0:
                num &= num - 1
                count += 1
            return count

        return sorted(sorted(arr), key=count_ones)
