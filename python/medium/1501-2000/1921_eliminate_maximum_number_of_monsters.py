from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        reach = sorted([d / s for d, s in zip(dist, speed)])
        for i, t in enumerate(reach):
            if t <= i:
                return i
        return i + 1
