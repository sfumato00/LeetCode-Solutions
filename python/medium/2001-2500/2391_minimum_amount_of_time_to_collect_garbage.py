from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        
        n = len(garbage)
        visited = set()
        travel_sum = [0] * n
        for i, tp in enumerate(travel):
            travel_sum[i + 1] = travel_sum[i] + tp

        ans = 0    
        for i in range(n - 1, -1, -1):
            x = garbage[i]
            ans += len(x)
            if len(visited) == 3:
                continue
            for tp in x:
                if tp not in visited:
                    ans += travel_sum[i]
                    visited.add(tp)

        return ans