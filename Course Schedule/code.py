class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)

        unvisited=0
        visiting=1
        visited=2
        states=[unvisited]*numCourses

        def dfs(node):
            state=states[node]
            if state==visited:
                return True
            elif state==visiting:
                return False

            states[node]=visiting  
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            states[node]=visited
            return True

        for i in range(numCourses):
            if not dfs(i):#means there is a cycle
                return False
        return True
