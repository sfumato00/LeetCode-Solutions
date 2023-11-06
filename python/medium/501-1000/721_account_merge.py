from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name_map = {}
        parents = {}

        for i, (name, *emails) in enumerate(accounts):
            for e in emails:
                parents[e] = e
                email_to_name_map[e] = name

        def find(parents, x):
            while parents[x] != x:
                x, parents[x] = parents[x], parents[parents[x]]
            return x

        def union(parents, x, y):
            p_x = find(parents, x)
            p_y = find(parents, y)
            if p_x != p_y:
                parents[p_y] = p_x

        for acc in accounts:
            n = len(acc)
            p = acc[1]
            for i in range(2, n):
                union(parents, acc[i], p)

        accts = defaultdict(list)
        for c, p in parents.items():
            # print(f"c: {c}, p: {p}")
            accts[find(parents, c)].append(c)

        return [[email_to_name_map[k]] + sorted(v) for k, v in accts.items()]
