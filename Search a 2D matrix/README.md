# Search in a 2D Matrix - Explanation

## Problem Statement
Given an `m x n` matrix where:
- Integers in each row are sorted from left to right.
- The first integer of each row is greater than the last integer of the previous row.

Write an algorithm that searches for a given `target` value in this matrix efficiently.

---

## Code Explanation (Line by Line)

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
```
- Defines a class `Solution`.
- Declares a function `searchMatrix` that takes two parameters:
  - `matrix`: A 2D list of integers (`List[List[int]]`).
  - `target`: An integer to search in the matrix.
- The function returns a boolean value (`True` if `target` is found, otherwise `False`).

```python
        m=len(matrix)
        n=len(matrix[0])
```
- `m` stores the number of rows in the matrix (`len(matrix)`).
- `n` stores the number of columns in the matrix (`len(matrix[0])`).

```python
        t=m*n
```
- Computes the total number of elements in the matrix (`t = m * n`).

```python
        left=0
        right=t-1
```
- Initializes `left` pointer to `0` (start of the flattened array representation of the matrix).
- Initializes `right` pointer to `t-1` (end of the flattened array representation of the matrix).

```python
        while left<=right:
```
- Starts a `while` loop that continues as long as `left` is less than or equal to `right`.
- This implements **Binary Search**, which ensures an efficient O(log(m*n)) time complexity.

```python
            mid=(left+right)//2
```
- Calculates the middle index `mid` of the search space using integer division.

```python
            i=mid//n
            j=mid%n
```
- Converts `mid` from a **1D index** into **2D coordinates**:
  - `i = mid // n` (Row index: How many full rows fit before `mid`).
  - `j = mid % n` (Column index: The remainder after dividing by `n`).

```python
            mid_value=matrix[i][j]
```
- Retrieves the matrix element at position `(i, j)`.

```python
            if mid_value==target:
                return True
```
- If the value at `mid` is equal to `target`, return `True` (found).

```python
            elif target<mid_value:
                right=mid-1
```
- If `target` is smaller than `mid_value`, discard the right half by updating `right = mid - 1`.

```python
            else:
                left=mid+1
```
- If `target` is greater than `mid_value`, discard the left half by updating `left = mid + 1`.

```python
        return False
```
- If the loop ends without finding `target`, return `False` (not found).

---

## Algorithm Summary
1. Convert the 2D matrix into a **conceptual 1D array** for binary search.
2. Use **binary search** to check the middle element and adjust search bounds accordingly.
3. Convert the **1D index** into **2D row-column coordinates**.
4. Return `True` if `target` is found, otherwise return `False`.

---

## Time & Space Complexity
- **Time Complexity**: **O(log(m*n))** (Binary Search in a sorted array)
- **Space Complexity**: **O(1)** (Constant extra space usage)

---

## Example
### Input
```python
matrix = [
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 60]
]
target = 3
```
### Execution
- `m = 3`, `n = 4`, `t = 12`
- `left = 0`, `right = 11`
- Binary search steps:
  1. `mid = 5`, element at `(1,1) = 11`, adjust `right = 4`
  2. `mid = 2`, element at `(0,2) = 5`, adjust `right = 1`
  3. `mid = 0`, element at `(0,0) = 1`, adjust `left = 1`
  4. `mid = 1`, element at `(0,1) = 3` (Found!)
### Output
```python
True
```

