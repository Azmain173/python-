# LeetCode 207: Course Schedule (DFS Approach)

## Problem Statement
You are given **numCourses** (total number of courses) and a list of **prerequisites**, where **prerequisites[i] = [a, b]** means that course **a** depends on course **b** (i.e., you must complete course **b** before taking course **a**).

Return **true** if it is possible to finish all courses, otherwise return **false** (which means there is a cycle in the dependency graph).

---

## **Approach: Depth-First Search (DFS) with Cycle Detection**
### **1. Graph Representation**
- The problem can be visualized as a **directed graph**, where:
  - **Nodes** represent courses.
  - **Edges** represent prerequisites (dependencies between courses).
- If there is a cycle in this graph, it is **impossible** to finish all courses.
- Otherwise, all courses can be completed.

### **2. Key Idea for Cycle Detection**
We use **DFS traversal** to detect cycles using **state tracking**:
- **Unvisited (0)** → Course has not been processed.
- **Visiting (1)** → Course is being processed in the current DFS path.
- **Visited (2)** → Course and all its prerequisites have been processed.

🚨 **Cycle Detection Rule:**
- If a node is **already `visiting` during DFS traversal**, it means we have revisited a node before finishing it → **Cycle found!**

---

## **Code Explanation**
```python
from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        # State tracking
        unvisited = 0
        visiting = 1
        visited = 2
        states = [unvisited] * numCourses

        # DFS function to check for cycles
        def dfs(node):
            state = states[node]
            if state == visited:
                return True  # Already processed, no cycle
            elif state == visiting:
                return False  # Cycle detected!

            states[node] = visiting  # Mark node as 'in-progress'
            for nei in graph[node]:
                if not dfs(nei):
                    return False  # If cycle is found in a neighbor, return False
            states[node] = visited  # Mark as fully processed
            return True

        # Run DFS on all nodes
        for i in range(numCourses):
            if not dfs(i):  # If a cycle is found, return False
                return False
        return True
```

---

## **Step-by-Step Execution**
Let's consider an example to see how this works.

### **Example Input:**
```python
numCourses = 3
prerequisites = [[0,1], [1,2], [2,0]]  # Cycle exists: 0 → 1 → 2 → 0
```

### **Step 1: Build Graph**
The graph representation:
```python
{
    0: [1],
    1: [2],
    2: [0]
}
```

### **Step 2: Run DFS on Each Node**
#### **DFS Traversal Process**
1. **Start DFS on `0` → Mark `0` as `visiting`**
2. **Go to `1` → Mark `1` as `visiting`**
3. **Go to `2` → Mark `2` as `visiting`**
4. **Go to `0` (again) → `0` is already `visiting`** → **Cycle detected!** 🚨
5. **Return `False` up the recursion stack** → `dfs(2) → dfs(1) → dfs(0)` return `False`.
6. **Final Result: `False` (Cannot finish all courses).**

---

## **Why Do We Need `visited`, `visiting`, and `unvisited`?**
The **three states** help in efficient cycle detection:
- **`unvisited (0)`** → Not yet processed.
- **`visiting (1)`** → Currently being processed (part of active DFS path).
- **`visited (2)`** → Fully processed (no cycle found in its DFS subtree).

🚨 **Cycle happens if we encounter a node that is still in the `visiting` state!**

### **Alternative Approaches**
Other ways to solve this problem:
- **Kahn's Algorithm (BFS-based Topological Sorting)**: Uses **indegree counts** to process courses with no prerequisites first.
- **Disjoint Set (Union-Find)**: Can also detect cycles, but DFS is more intuitive for graph problems.

---

## **Time Complexity Analysis**
- **Building the Graph:** `O(E)`, where `E` is the number of prerequisites.
- **DFS Traversal:** `O(V + E)`, where `V` is the number of courses (nodes), and `E` is the number of prerequisites (edges).
- **Overall Complexity:** `O(V + E)`.

## **Space Complexity Analysis**
- **Graph Storage:** `O(E)`.
- **State Tracking:** `O(V)`.
- **Recursive Stack (Worst Case - DFS on all nodes):** `O(V)`.
- **Total Space:** `O(V + E)`.

---

## **Final Thoughts**
- We used **DFS with state tracking** to efficiently detect cycles in the prerequisite graph.
- The key idea is **marking nodes as `visiting` during DFS traversal**.
- If we encounter a `visiting` node again, it means there is a **cycle** → return `False`.
- If we finish DFS traversal without finding a cycle, return `True` (courses can be completed).

📌 **This is an elegant and efficient way to detect cycles in a directed graph using DFS!** 🚀

