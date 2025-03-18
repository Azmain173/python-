# README for LeetCode 200: Number of Islands

## Problem Statement
Given an `m x n` grid filled with '1' (land) and '0' (water), we need to count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. We use Depth-First Search (DFS) to traverse and mark visited lands.

---

## Code Explanation

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])  # Get the dimensions of the grid

        def dfs(i, j):  # Define DFS function
            # Base case: If out of bounds or water, stop recursion
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return  # Simply exit the function without returning anything
            
            grid[i][j] = "0"  # Mark the cell as visited
            
            # Recursively explore all four possible directions
            dfs(i, j + 1)  # Explore right
            dfs(i, j - 1)  # Explore left
            dfs(i - 1, j)  # Explore up
            dfs(i + 1, j)  # Explore down

        num_island = 0  # Counter for number of islands
        for i in range(m):  # Iterate over all rows
            for j in range(n):  # Iterate over all columns
                if grid[i][j] == "1":  # Found an unvisited island
                    num_island += 1  # Increase island count
                    dfs(i, j)  # Call DFS to mark the entire island as visited
        
        return num_island  # Return the total number of islands
```

---

## **Breaking Down the DFS Function**

```python
def dfs(i, j):
    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
        return  
```
- If the current cell is **out of bounds** or **not land ('1')**, we exit the function. This prevents unnecessary recursion.
- `return` **does not** mean `return False`—it simply exits the function without returning anything.

```python
grid[i][j] = "0"
```
- Marks the cell as **visited** so that it is not counted again.
- This helps in preventing duplicate island counts.

```python
dfs(i, j + 1)  # Explore right
dfs(i, j - 1)  # Explore left
dfs(i - 1, j)  # Explore up
dfs(i + 1, j)  # Explore down
```
- Calls `dfs` on all four **adjacent** cells.
- Since an island is formed by **connected '1's**, we must visit all of them.

---

## **Why No `else` Statement?**
There is no need for an `else` statement because:
- If the base condition (`if i < 0 ... or grid[i][j] != "1"`) is met, the function **already exits** (`return`).
- If the base condition is **not met**, the function **continues execution normally**, marking the land and making recursive calls.
- Adding `else` would be redundant.

---

## **Example Walkthrough**
### **Example 1:**
#### **Input:**
```python
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
```
#### **Visualization:**
```
1  1  0  0  0
1  1  0  0  0
0  0  1  0  0
0  0  0  1  1
```
#### **Process:**
1. **First Island:** Start at `(0,0)`, mark connected '1's as '0'.
2. **Second Island:** Find '1' at `(2,2)`, mark connected '1's.
3. **Third Island:** Find '1' at `(3,3)`, mark connected '1's.

#### **Output:**
```python
3
```

---

## **Time & Space Complexity**
- **Time Complexity:** `O(m * n)` – Each cell is visited at most once.
- **Space Complexity:** `O(m * n)` – In the worst case (all land), DFS recursion depth reaches `m * n`.

This solution effectively counts the number of islands using **Depth-First Search (DFS) traversal** while modifying the grid in place.

---

