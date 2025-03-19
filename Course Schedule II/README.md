# Course Schedule II - LeetCode 210

## Problem Statement
You are given `numCourses` courses labeled from `0` to `numCourses - 1`. You are also given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` before course `ai`.

Return the ordering of courses you should take to finish all courses. If it is impossible to finish all courses, return an empty list.

---

## Approach: DFS with Topological Sorting
This solution uses **Depth-First Search (DFS) with cycle detection** to determine the correct ordering of courses.

### **Step 1: Graph Construction**
We represent the course dependencies as a **directed graph** where:
- Each course is a node.
- Each prerequisite `[a, b]` means an edge from `b → a` (course `b` must be taken before `a`).
- We store this graph as an adjacency list.

### **Step 2: Cycle Detection with DFS**
- We maintain a `states` array where:
  - `0` (unvisited): The node has not been processed yet.
  - `1` (visiting): The node is being visited in the current DFS path (used for cycle detection).
  - `2` (visited): The node and all its dependencies are fully processed.
- If a node is encountered in the `visiting` state, it means a cycle exists, and we return an empty list.

### **Step 3: Topological Sorting (DFS Post-order Traversal)**
- If a course has no dependencies, we add it to the `order` list after visiting all its prerequisites.
- Since we push a course **after visiting all its dependencies**, we need to **reverse** the final `order` list to get the correct topological order.

---

## **Code Explanation**

```python
from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = 2
        unvisited = 0
        visiting = 1

        graph = defaultdict(list)
        for v, u in prerequisites:  # Reverse the direction to match topological sorting
            graph[u].append(v)

        states = [unvisited] * numCourses  # Initialize state array
        order = []

        def dfs(node):
            state = states[node]
            if state == visited:
                return True
            elif state == visiting:
                return False  # Cycle detected

            states[node] = visiting  # Mark node as visiting
            for nei in graph[node]:
                if not dfs(nei):
                    return False

            states[node] = visited  # Mark node as visited
            order.append(node)  # Add node after visiting all dependencies
            return True

        for i in range(numCourses):
            if states[i] == unvisited:  # Only visit unvisited nodes
                if not dfs(i):
                    return []  # Cycle detected, return empty list

        return order[::-1]  # Reverse order for correct topological sorting
```

---

## **Why `order[::-1]`?**
Since we add courses **after processing their dependencies**, the resulting list is in **reverse topological order**. Thus, we need to reverse it at the end.

---

## **Time and Space Complexity**
- **Time Complexity:** `O(V + E)`, where `V` is the number of courses (nodes) and `E` is the number of prerequisites (edges).
- **Space Complexity:** `O(V + E)` for storing the graph and `O(V)` for the recursion stack in the worst case.

---

## **Example Walkthrough**

### **Input 1:**
```python
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
```

### **Graph Representation:**
```
    0 → 1 → 3
    0 → 2 → 3
```

### **DFS Traversal Order:**
1. Start DFS at `0` → Explore `1` → Explore `3` (added to order)
2. Explore `2` → Explore `3` (already visited)
3. Add `2`, then `1`, then `0`
4. **Final order:** `[0, 2, 1, 3]`

### **Output:**
```python
[0, 2, 1, 3]
```

---

## **Edge Cases**
✅ No prerequisites → Return `[0, 1, 2, ..., numCourses-1]`  
✅ One large chain of dependencies → Works fine as long as acyclic  
✅ Cycle exists → Returns `[]`  
✅ Disconnected graph (independent courses) → Works fine  

---

## **Conclusion**
This solution efficiently finds a valid course order (if possible) using **DFS-based topological sorting** while handling cycles. 🚀

