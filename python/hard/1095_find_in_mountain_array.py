# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        ma = mountain_arr
        n = ma.length()
        arr = [None] * n

        def find_peak():
            lo, hi = 0, n
            while lo < hi:
                m = (lo + hi) // 2
                if not arr[m]:
                    arr[m] = ma.get(m)
                if m - 1 >= 0 and not arr[m - 1]:
                    arr[m - 1] = ma.get(m - 1)
                if m + 1 < n and not arr[m + 1]:
                    arr[m + 1] = ma.get(m + 1)

                if m - 1 >= 0 and m + 1 < n and arr[m - 1] < arr[m] > arr[m + 1]:
                    return m
                if (m + 1 == n or arr[m] > arr[m + 1]) and (
                    m - 1 >= 0 and arr[m - 1] > arr[m]
                ):
                    hi = m
                else:
                    lo = m + 1
            return lo

        peak = find_peak()
        if not arr[peak]:
            arr[peak] = self.get(peak)
        if arr[peak] == target:
            return peak

        def search_left():
            lo, hi = 0, peak
            while lo < hi:
                m = (lo + hi) // 2
                if not arr[m]:
                    arr[m] = ma.get(m)

                if arr[m] == target:
                    return m

                if target < arr[m]:
                    hi = m
                else:
                    lo = m + 1
            return lo

        def search_right():
            lo, hi = peak + 1, n
            while lo < hi:
                m = (lo + hi) // 2
                if not arr[m]:
                    arr[m] = ma.get(m)

                if arr[m] == target:
                    return m

                if target >= arr[m]:
                    hi = m
                else:
                    lo = m + 1
            return lo

        left = search_left()
        if arr[left] == target:
            return left
        right = search_right()
        if right < n and arr[right] == target:
            return right
        return -1
