# Spiral Matrix Algorithm

## Problem Statement
Given an `m x n` matrix, return all elements in **spiral order**, starting from the top-left corner.

---

## **Code Explanation (Line-by-Line)**

### **1. Class Definition and Function Signature**
```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
```
- `Solution` class is defined to follow LeetCode's standard structure.
- `spiralOrder` function takes a **2D list (`matrix`)** as input.
- The function returns a **1D list**.
- `List[List[int]]` and `List[int]` are **type hints** to indicate input and output formats.

---

### **2. Variable Initialization**
```python
m, n = len(matrix), len(matrix[0])
ans = []
i, j = 0, 0
UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
direction = RIGHT
```
- `m, n` store the **number of rows and columns** in the matrix.
- `ans = []` initializes an **empty list** to store the result.
- `i, j = 0, 0` initializes **row (`i`) and column (`j`)** starting from the top-left corner `(0,0)`.
- `UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3` defines **direction constants**.
- `direction = RIGHT` sets the **initial movement direction** to **right**.

---

### **3. Boundary Initialization**
```python
UP_WALL = 0
RIGHT_WALL = n
DOWN_WALL = m
LEFT_WALL = -1
```
- Defines **boundaries** to prevent revisiting elements.
  - `UP_WALL = 0`: The upper limit of movement.
  - `RIGHT_WALL = n`: Right boundary starts at `n` (out of bounds).
  - `DOWN_WALL = m`: Bottom boundary starts at `m` (out of bounds).
  - `LEFT_WALL = -1`: Left boundary starts at `-1` (before the first column).

---

### **4. Main Loop - Spiral Traversal**
```python
while len(ans) != m*n:
```
- The loop **runs until all elements (`m*n`) are added** to `ans`.

---

### **5. Direction Handling**
#### **Move Right**
```python
if direction == RIGHT:
    while j < RIGHT_WALL:
        ans.append(matrix[i][j])
        j += 1
    i, j = i+1, j-1
    RIGHT_WALL -= 1
    direction = DOWN
```
- Moves **right** across the current row.
- Stops at **`RIGHT_WALL`**.
- **Adjustments:** Move down and shift right boundary (`RIGHT_WALL -= 1`).
- **Next direction:** **DOWN**.

---

#### **Move Down**
```python
elif direction == DOWN:
    while i < DOWN_WALL:
        ans.append(matrix[i][j])
        i += 1
    i, j = i-1, j-1
    DOWN_WALL -= 1
    direction = LEFT
```
- Moves **down** the column.
- Stops at **`DOWN_WALL`**.
- **Adjustments:** Move left and shift bottom boundary (`DOWN_WALL -= 1`).
- **Next direction:** **LEFT**.

---

#### **Move Left**
```python
elif direction == LEFT:
    while j > LEFT_WALL:
        ans.append(matrix[i][j])
        j -= 1
    i, j = i-1, j+1
    LEFT_WALL += 1
    direction = UP
```
- Moves **left** across the row.
- Stops at **`LEFT_WALL`**.
- **Adjustments:** Move up and shift left boundary (`LEFT_WALL += 1`).
- **Next direction:** **UP**.

---

#### **Move Up**
```python
else:
    while i > UP_WALL:
        ans.append(matrix[i][j])
        i -= 1
    i, j = i+1, j+1
    UP_WALL += 1
    direction = RIGHT
```
- Moves **up** the column.
- Stops at **`UP_WALL`**.
- **Adjustments:** Move right and shift top boundary (`UP_WALL += 1`).
- **Next direction:** **RIGHT**.

---

### **6. Return the Result**
```python
return ans
```
- **Returns** the final list containing elements in **spiral order**.

---

### **7. Time & Space Complexity**
```python
# Time: O(m*n) 
# Space: O(1)
```
- **Time Complexity:** \(O(m 	imes n)\) (each element is visited **once**).
- **Space Complexity:** \(O(1)\) (only a few extra variables are used).

---

## **Example**
### **Input:**
```python
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]
```
### **Output:**
```python
[1, 2, 3, 6, 9, 8, 7, 4, 5]
```

---

## **Edge Cases Considered**
1. **Single Row:** `[[1, 2, 3, 4]]`
2. **Single Column:** `[[1], [2], [3], [4]]`
3. **Empty Matrix:** `[]`
4. **Square Matrix:** `[[1,2],[3,4]]`

---

## **Final Thoughts**
- Your approach is **logically correct** but could use some boundary refinements.
- A more conventional approach would set `RIGHT_WALL = n-1` instead of `n` for clarity.

This README provides **a structured breakdown of each line**, making it easy to understand your algorithm. 🚀
