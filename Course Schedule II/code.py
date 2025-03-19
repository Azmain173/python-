class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited=2
        unvisited=0
        visiting=1

        graph=defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)
        
        states=[unvisited]*numCourses
        order=[]

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
            order.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return order
