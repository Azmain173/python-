# Rotate Image - Explanation

## Problem Statement
Given an `n x n` 2D matrix representing an image, rotate the image **90 degrees clockwise** **in-place** (without using extra memory for another matrix).

---

## Code Explanation (Line by Line)

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
```
- Defines a class `Solution`.
- Declares a function `rotate` that takes a `matrix` (a 2D list of integers) as input.
- The function **modifies the matrix in-place**, meaning no additional matrix storage is used.

```python
        """
        Do not return anything, modify matrix in-place instead.
        """
```
- This is a docstring explaining that the function modifies `matrix` directly instead of returning a new matrix.

```python
        n=len(matrix)
```
- Determines the size `n` of the `n x n` matrix.

---

## Step 1: Transpose the Matrix

```python
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
```
### What is Transposition?
- The **transpose** of a matrix swaps its rows with its columns.
- The element at position `(i, j)` swaps with the element at `(j, i)`.

### Explanation of Code:
1. **Outer loop**: Iterates over rows `i` from `0` to `n-1`.
2. **Inner loop**: Iterates over columns `j` from `i+1` to `n-1`.
   - Why start from `i+1`? Because swapping elements below the diagonal would undo previous swaps.
   - Example: If we swap `(0,1)` with `(1,0)`, then when `i=1` and `j=0`, swapping `(1,0)` with `(0,1)` would reverse the swap.
   - This ensures **each pair is swapped only once**, avoiding redundant operations.
3. **Swap operation:** `matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]`.
   - Exchanges element `(i, j)` with `(j, i)`.

### Example Before and After Transposition:
#### **Before Transposition:**
```
1  2  3
4  5  6
7  8  9
```
#### **After Transposition:**
```
1  4  7
2  5  8
3  6  9
```

---

## Step 2: Horizontal Reflection

```python
        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-j-1]=matrix[i][n-j-1],matrix[i][j]
```

### What is Horizontal Reflection?
- Each row is **reversed** by swapping the leftmost and rightmost elements.
- The first column swaps with the last column, the second swaps with the second-last, and so on.

### Explanation of Code:
1. **Outer loop**: Iterates over all rows (`i` from `0` to `n-1`).
2. **Inner loop**: Iterates over half of the columns (`j` from `0` to `n//2`).
3. **Swap operation:** `matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]`.
   - Swaps element `(i, j)` with `(i, n-j-1)`.
   - `n//2` ensures we only swap **half the row** to avoid undoing swaps.

### Example Before and After Horizontal Reflection:
#### **Before Horizontal Reflection:**
```
1  4  7
2  5  8
3  6  9
```
#### **After Horizontal Reflection:**
```
7  4  1
8  5  2
9  6  3
```

---

## Why `n//2` in the Reflection?
- A row of size `n` needs **only half** its elements swapped (mirrored effect).
- If `n = 3`, then `n//2 = 1`, meaning we swap the **first** and **last** columns.
- If `n = 4`, then `n//2 = 2`, meaning we swap the **first two** columns with the last two.

## Why `n-j-1`?
- `n-j-1` gives the **last column index corresponding to `j`**.
- If `j = 0`, then `n-0-1 = n-1` (last column index).
- If `j = 1`, then `n-1-1 = n-2` (second-last column index).

---

## Time & Space Complexity
- **Time Complexity**: **O(n²)** (Each element is accessed once during transposition and once during reflection).
- **Space Complexity**: **O(1)** (In-place modification, no extra space used).

---

## Example
### Input
```python
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
```
### Execution
#### **Step 1: Transposition**
```
1  4  7
2  5  8
3  6  9
```
#### **Step 2: Horizontal Reflection**
```
7  4  1
8  5  2
9  6  3
```
### Output
```python
matrix = [
  [7, 4, 1],
  [8, 5, 2],
  [9, 6, 3]
]
```

This is the **90-degree clockwise rotation** of the original matrix.

