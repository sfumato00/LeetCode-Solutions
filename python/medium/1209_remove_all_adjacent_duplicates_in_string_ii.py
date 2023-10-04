class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        for ch in s:
            if stk and ch == stk[-1][0]:
                stk[-1][1] += 1
            else:
                stk.append([ch, 1])
            if stk[-1][1] == k:
                stk.pop()

        return "".join([x * cnt for x, cnt in stk])
