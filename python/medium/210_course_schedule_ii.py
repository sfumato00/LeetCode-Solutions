from collections import defaultdict, deque
from typing import List


class DfsSolution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for course, prerequisite in prerequisites:
            graph[prerequisite] += [course]

        def dfs(prerequisite, visited, in_stack, ans):
            if visited[prerequisite]:
                return True

            if in_stack[prerequisite]:
                return False

            in_stack[prerequisite] = True
            for course in graph[prerequisite]:
                if not dfs(course, visited, in_stack, ans):
                    return False

            in_stack[prerequisite] = False
            visited[prerequisite] = True
            ordered_courses.append(prerequisite)
            return True

        ordered_courses, visited, in_stack = (
            [],
            [False] * numCourses,
            [False] * numCourses,
        )
        for course in range(numCourses):
            if not dfs(course, visited, in_stack, ordered_courses):
                return []

        return ordered_courses[::-1]


class BfsSolution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degrees = [0] * numCourses
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre] += [course]
            in_degrees[course] += 1

        ordered_courses = [c for c, degree in enumerate(in_degrees) if degree == 0]
        d_q = deque(ordered_courses)
        while d_q:
            pre = d_q.popleft()
            for course in graph[pre]:
                in_degrees[course] -= 1
                if in_degrees[course] == 0:
                    d_q += [course]
                    ordered_courses += [course]

        return ordered_courses if len(ordered_courses) == numCourses else []
