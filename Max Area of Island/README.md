# LeetCode 695: Max Area of Island - README

## Problem Statement
You are given an `m x n` binary grid representing a map of islands (`1`s) and water (`0`s). An island is formed by connecting adjacent lands horizontally or vertically. The task is to find the area of the largest island in the grid.

## Solution Explanation

### 1. Understanding the Approach
- We use **Depth-First Search (DFS)** to explore each island and calculate its area.
- Once a land cell (`1`) is found, we start a DFS traversal from that cell, marking visited cells as `0` to avoid recounting.
- The DFS function recursively counts all connected `1`s and returns the total size of the island.
- We iterate through the grid, calling DFS on each unvisited land cell, and keep track of the maximum area found.

### 2. Code Breakdown
```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])  # Get the dimensions of the grid

        def dfs(i, j):  # Depth-First Search function
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0  # Stop DFS if out of bounds or water encountered
            
            grid[i][j] = 0  # Mark the cell as visited
            return 1 + dfs(i, j + 1) + dfs(i, j - 1) + dfs(i + 1, j) + dfs(i - 1, j)

        max_area = 0  # Variable to track the maximum island area
        for i in range(m):  # Iterate over all rows
            for j in range(n):  # Iterate over all columns
                if grid[i][j] == 1:  # If land is found
                    max_area = max(max_area, dfs(i, j))  # Update max area with DFS result
        
        return max_area  # Return the largest island area found
```

### 3. Detailed Explanation of DFS
```python
        def dfs(i, j):  # Depth-First Search function
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0  # Stop DFS if out of bounds or water encountered
            
            grid[i][j] = 0  # Mark the cell as visited to prevent duplicate counting
            
            return 1 + dfs(i, j + 1) + dfs(i, j - 1) + dfs(i + 1, j) + dfs(i - 1, j)
```
- The function **checks if the current cell is out of bounds or is water (`0`)**. If so, it stops.
- Otherwise, it **marks the current land cell as visited (`0`)** to prevent revisits.
- It **recursively explores all four adjacent cells** (right, left, down, up), adding up the area of the connected island.
- The **return statement** accumulates the size of the island by adding `1` (for the current cell) and the results of DFS calls.

### 4. Why No `else` Statement?
- The `return` inside the `if` block stops the function if the cell is water or out of bounds.
- If execution reaches beyond the `if`, it means the cell is land, and the function continues.
- Using `else` here would be redundant, as the second part of the function only executes when the `if` condition is false.

### 5. Why `return 0` Instead of `return False`?
- The function **counts** the number of land cells, so we return `0` when a base case is met (out of bounds or water).
- Returning `False` wouldn't work because we need numerical values to compute island size.

### 6. Example Walkthrough
#### Example 1
**Input:**
```python
[[0,0,1,0,0],
 [0,1,1,1,0],
 [0,0,1,0,0],
 [0,0,0,0,0]]
```
**DFS Execution:**
- Starts at `grid[0][2]`, marking it as `0`.
- Moves to `grid[1][2]`, marking it as `0`.
- Moves to `grid[1][1]`, `grid[1][3]`, `grid[2][2]`... all marked as `0`.
- Stops when no more connected `1`s are found.
- Total area of this island: **5**

**Output:** `5`

#### Example 2
**Input:**
```python
[[1,1,0,0,0],
 [1,1,0,0,0],
 [0,0,0,1,1],
 [0,0,0,1,1]]
```
**DFS Execution:**
- First island (top-left): area = `4`
- Second island (bottom-right): area = `4`
- **Maximum area:** `4`

**Output:** `4`

## 7. Complexity Analysis
- **Time Complexity:** `O(m * n)`, where `m` is the number of rows and `n` is the number of columns. Every cell is visited at most once.
- **Space Complexity:** `O(m * n)` in the worst case (if all cells are land, DFS recursion goes that deep).

## 8. Summary
- **DFS is used to explore all connected land cells and count their total area.**
- **Grid cells are marked as `0` (visited) to prevent duplicate counting.**
- **The largest island area is tracked and returned.**

This solution efficiently finds the largest island in a given grid using DFS recursion. 🚀

