# Binary Search - LeetCode Problem

## Problem Statement
Given a **sorted** array of integers `nums` and an integer `target`, implement a function that searches for `target` in `nums` using **binary search**. If `target` exists, return its **index**; otherwise, return `-1`.

### Example 1:
**Input:**
```python
nums = [-1,0,3,5,9,12]
target = 9
```
**Output:** `4`

### Example 2:
**Input:**
```python
nums = [-1,0,3,5,9,12]
target = 2
```
**Output:** `-1`

---

## Approach
### **Binary Search Algorithm**
1. **Initialize Pointers:**
   - Set `left = 0` and `right = len(nums) - 1`.
   
2. **Iterate Until `left` ≤ `right`**:
   - Find the middle index: `mid = (left + right) // 2`.
   - If `nums[mid]` is equal to `target`, return `mid`.
   - If `nums[mid]` is less than `target`, move `left` to `mid + 1`.
   - Else, move `right` to `mid - 1`.

3. **Return `-1` if the target is not found**.

---

## Corrected Python Code
```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2  # Recalculate mid in each iteration
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1  # Target not found
```

---

## Common Mistakes & Fixes
### ❌ Mistake 1: **Calculating `mid` Only Once**
```python
mid = (right + left + 1) // 2  # Incorrectly placed outside the loop
```
✅ **Fix:** Move `mid` calculation **inside the loop** so it updates dynamically.

---

### ❌ Mistake 2: **Incorrect Condition for Updating Pointers**
```python
elif nums[left] < target:  # Wrong comparison, should be nums[mid]
    left = mid + 1
```
✅ **Fix:** Compare `target` with `nums[mid]`, not `nums[left]`.

---

### ❌ Mistake 3: **Premature Return Statement**
```python
return -1  # Placed inside the loop, causing early exit
```
✅ **Fix:** Move `return -1` **outside the loop** to ensure full search execution.

---

## Time & Space Complexity
- **Time Complexity:** `O(log N)`, where `N` is the number of elements in `nums`.
- **Space Complexity:** `O(1)`, since no extra space is used.

---

## Alternative Approach: Recursive Binary Search
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if left > right:
                return -1
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, right)
            else:
                return binary_search(left, mid - 1)
        
        return binary_search(0, len(nums) - 1)
```
**Pros:** Elegant, follows recursion.
**Cons:** Uses extra stack space `O(log N)` due to recursion.

---

## Summary
✅ **Binary search is an efficient method** for finding an element in a sorted array.
✅ **Iterative implementation is preferred** due to its `O(1)` space complexity.
✅ **Avoid common pitfalls** like incorrect `mid` calculations and misplaced `return` statements.

---

### 🚀 Happy Coding!

