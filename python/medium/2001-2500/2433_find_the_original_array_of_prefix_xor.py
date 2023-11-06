from typing import List


class Solution:
    """_summary_
    pref[i] = arr[0] ^ arr[1] ... ^ arr[i]
    pref[i + 1] = arr[0] ^ arr[1] ... ^ arr[i] ^ arr[i + 1]

    pref[i] ^ pref[i + 1]
        = (arr[0] ^ arr[1] ... ^ arr[i]) ^ (arr[0] ^ arr[1] ... ^ arr[i] ^ arr[i + 1])
        = (arr[0] ^ arr[0]) ^ (arr[1] ^ arr[1]) ... ^ (arr[i] ^ arr[i]) ^ arr[i + 1]
        = arr[i + 1]

    i.e. arr[i] = pref[i - 1] ^ pref[i]
    """

    def findArray(self, pref: List[int]) -> List[int]:
        return pref[0:1] + [a ^ b for a, b in zip(pref[:-1], pref[1:])]
