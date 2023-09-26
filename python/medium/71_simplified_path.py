class Solution:
    def simplifyPath(self, path: str) -> str:
        terms = path.split("/")
        stk = []
        for x in terms:
            if x in ["/", ".", ""]:
                continue
            if x == "..":
                if stk:
                    stk.pop()
            else:
                stk.append(x)
        return "/" + "/".join(stk)
