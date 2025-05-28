class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[pre].append(course)

        visited = [0] * numCourses  
        result = []
        has_cycle = False

        def dfs(course):
            nonlocal has_cycle
            if visited[course] == 1:
                has_cycle = True
                return
            if visited[course] == 2:
                return

            visited[course] = 1 
            for neighbor in graph[course]:
                dfs(neighbor)
                if has_cycle:
                    return
            visited[course] = 2
            result.append(course)

        for i in range(numCourses):
            if visited[i] == 0:
                dfs(i)
            if has_cycle:
                return []

        return result[::-1]  
