from math import inf
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        M, N = len(A), len(B)
        if M > N:
            M, N = N, M
            A, B = B, A

        L = M + N
        half = L // 2

        lo, hi = 0, M - 1  # edge case: A = []
        while True:
            i = (lo + hi) // 2
            j = half - i - 2  # the key idea

            leftA = A[i] if i >= 0 else -inf
            rightA = A[i + 1] if i + 1 < M else inf
            leftB = B[j] if j >= 0 else -inf
            rightB = B[j + 1] if j + 1 < N else inf

            if leftA <= rightB and leftB <= rightA:
                break

            if leftA <= rightB:
                lo = i + 1
            else:
                hi = i - 1

        if L % 2:
            return min(rightA, rightB)
        return (max(leftA, leftB) + min(rightA, rightB)) / 2
