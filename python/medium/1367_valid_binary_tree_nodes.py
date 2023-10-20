from typing import List


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        visited, in_stack = [False] * n, [False] * n
        indegree = [0] * n

        def dfs(u):
            if visited[u]:
                return True

            if in_stack[u]:
                return False

            in_stack[u] = True

            if leftChild[u] != -1:
                indegree[leftChild[u]] += 1
                if not dfs(leftChild[u]):
                    return False

            if rightChild[u] != -1:
                indegree[rightChild[u]] += 1
                if not dfs(rightChild[u]):
                    return False

            visited[u] = True
            in_stack[u] = False
            return True

        for x in range(n):
            if visited[x]:
                continue

            if not dfs(x):
                return False

        num_of_root = 0
        for i in range(n):
            if indegree[i] > 1:
                return False
            num_of_root += 0 if indegree[i] else 1
        return num_of_root == 1
