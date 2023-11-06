class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        to_remove = set()
        for i, x in enumerate(s):
            if x == "(":
                stk.append(i)
            elif x == ")":
                if not stk:
                    to_remove.add(i)
                else:
                    stk.pop()
        while stk:
            to_remove.add(stk.pop())
        return "".join([x for i, x in enumerate(s) if i not in to_remove])
