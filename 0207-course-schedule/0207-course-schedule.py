class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i: [] for i in range(numCourses)} 

        for c, p in prerequisites:
            graph[c].append(p)

        visited = [0] * numCourses 

        def has_cycle(course): 
            if visited[course] == 1: 
                return True 
            
            if visited[course] == 2: 
                return False 

            visited[course] = 1 

            for p in graph[course]: 
                if has_cycle(p):
                    return True 

            visited[course] = 2
            return False 

        for i in range(numCourses):
            if has_cycle(i):
                return False
        return True