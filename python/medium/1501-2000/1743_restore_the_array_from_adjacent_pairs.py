from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        
        mem = defaultdict(list)
        for x, y in adjacentPairs:
            mem[x] += [y]
            mem[y] += [x]

        prev, curr = None, next(k for k, v in mem.items() if len(v) == 1)
        output = [curr]
        while len(output) < len(mem):
            for _next in mem[curr]:
                if _next != prev:
                    prev, curr = curr, _next
                    output += [_next]
                    break
        return output
