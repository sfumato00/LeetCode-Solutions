# https://leetcode.com/problems/kth-largest-element-in-an-array/description/

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.count_sort(nums, k)

    def heap(self, nums: List[int], k: int):
        min_heap = []
        for x in nums:
            heapq.heappush(min_heap, x)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return heapq.heappop(min_heap)

    def count_sort(self, nums: List[int], k: int):
        OFFSET = 10000
        N = OFFSET * 2 + 1
        arr = [0] * N
        for x in nums:
            arr[x + OFFSET] += 1
        for i in range(N - 1, -1, -1):
            x = arr[i]
            if x >= k:
                return i - OFFSET
            k -= x
        return -1