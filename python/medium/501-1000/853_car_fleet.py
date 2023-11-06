from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n = len(position)
        # maxHeap = [(-position[i], i) for i in range(n)]
        # heapq.heapify(maxHeap)
        # ans = n
        # while maxHeap:
        #     pos, i = heapq.heappop(maxHeap)
        #     h = (target + pos) / speed[i]

        #     while maxHeap and position[maxHeap[0][1]] + speed[maxHeap[0][1]] * h >= target:
        #         heapq.heappop(maxHeap)
        #         ans -= 1

        # return ans

        n = len(position)
        stk = [(i, (target - position[i]) / speed[i]) for i in range(n)]
        stk.sort(key=lambda x: position[x[0]])
        ans = 0
        while stk:
            head_of_fleet = stk.pop()
            while stk and stk[-1][1] <= head_of_fleet[1]:
                stk.pop()
            ans += 1
        return ans
