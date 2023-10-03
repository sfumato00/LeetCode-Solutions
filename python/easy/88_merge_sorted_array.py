from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k, i, j = len(nums1) - 1, m - 1, n - 1
        while i >= 0 or j >= 0:
            if j < 0 or (i >= 0 and nums1[i] >= nums2[j]):
                nums1[k], i = nums1[i], i - 1
            else:
                nums1[k], j = nums2[j], j - 1
            k -= 1
