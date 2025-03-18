# README - LeetCode 1971: Find if Path Exists in Graph

## Problem Statement
Given an undirected graph with `n` nodes and `edges` representing the connections between them, determine if there exists a valid path from the `source` node to the `destination` node.

### Example:
#### Input:
```python
n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5
```
#### Output:
```python
False
```

---

## Code Explanation

```python
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
```
- We define a function `validPath` that takes in the number of nodes `n`, a list of `edges`, and two nodes: `source` and `destination`.
- The goal is to determine if there is a path from `source` to `destination`.

### Base Case
```python
        if source == destination:
            return True
```
- If the `source` and `destination` are the same, we immediately return `True` because a node always has a valid path to itself.

### Graph Representation
```python
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
```
- We use a dictionary (`defaultdict`) to store an adjacency list representation of the graph.
- Since the graph is **undirected**, we add each edge in both directions (`u -> v` and `v -> u`).

### DFS Implementation
```python
        seen = set()
        seen.add(source)
```
- We initialize a `seen` set to track visited nodes to avoid infinite loops.
- The `source` node is added to `seen` since we are starting from it.

```python
        def dfs(i):
            if i == destination:
                return True
```
- We define a helper function `dfs(i)`, where `i` represents the current node.
- If we reach the `destination`, return `True`.

```python
            for nei in graph[i]:
                if nei not in seen:
                    seen.add(nei)
                    if dfs(nei):
                        return True
```
- We iterate through the neighbors (`nei`) of node `i`.
- If a neighbor has not been visited, we add it to the `seen` set and recursively call `dfs(nei)`. If `dfs(nei)` finds a path, we return `True`.

```python
            return False
```
- If no valid path is found, return `False`.

### Start DFS
```python
        return dfs(source)
```
- We start DFS from the `source` node.

---

## Time and Space Complexity Analysis
- **Time Complexity:** `O(n + e)`, where `n` is the number of nodes and `e` is the number of edges (we visit each node and edge once in DFS).
- **Space Complexity:** `O(n + e)`, since we store the graph in an adjacency list and keep track of visited nodes.

---

## Alternative Approaches
### BFS (Breadth-First Search)
Instead of DFS, we can use a queue to perform BFS, ensuring we explore all possible paths level by level.
```python
from collections import deque, defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        queue = deque([source])
        seen = set([source])
        
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append(nei)
        
        return False
```

---

## Related Problems
- **LeetCode 200 - Number of Islands** (DFS/BFS traversal in a grid)
- **LeetCode 547 - Number of Provinces** (Finding connected components in a graph)
- **LeetCode 133 - Clone Graph** (Graph traversal using DFS/BFS)
- **LeetCode 695 - Max Area of Island** (DFS on a grid-based graph)

---

This solution effectively determines if a path exists in an undirected graph using DFS. The BFS alternative provides another approach for solving the same problem.

