class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        for i, ch in enumerate(s):
            if not stk or ch != stk[-1]:
                stk.append(ch)
            else:
                stk.pop()
        return "".join(stk)
