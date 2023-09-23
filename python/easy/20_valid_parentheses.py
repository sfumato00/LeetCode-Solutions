class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "]": "[", "}": "{"}
        stk = []
        for ch in s:
            if stk and ch in dic and dic[ch] == stk[-1]:
                stk.pop()
            elif ch in dic:
                return False
            else:
                stk += [ch]
        return not stk
