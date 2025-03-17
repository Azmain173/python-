# LeetCode 49: Permutations - Solution Explanation

## Problem Statement
Given an array `nums` of **distinct integers**, return **all possible permutations** of the elements.

### Example:
#### Input:
```python
nums = [1,2,3]
```
#### Output:
```python
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

---

## Code Implementation
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)  # Get the length of the input list
        sol, res = [], []  # sol stores the current permutation, res stores all permutations

        def backtrack():
            if len(sol) == n:  # Base case: If sol has all elements, it's a valid permutation
                res.append(sol[:])  # Append a copy of sol to res
                return
                
            for x in nums:  # Iterate through all numbers in nums
                if x not in sol:  # Ensure we don't add duplicate numbers in the same permutation
                    sol.append(x)  # Add x to the current permutation
                    backtrack()  # Recursively build the permutation
                    sol.pop()  # Remove last element to backtrack
        
        backtrack()
        return res  # Return all generated permutations
```

---

## Explanation with Example
Let's walk through the execution of the function when `nums = [1,2,3]`.

### Step 1: Initial State
- `sol = []` (empty list, no numbers chosen yet)
- `res = []` (empty list, no permutations found yet)
- Start calling `backtrack()`

### Step 2: Building Permutations

1. Choose `1`: `sol = [1]`
   - Choose `2`: `sol = [1,2]`
     - Choose `3`: `sol = [1,2,3]` (Valid permutation, store in `res`)
     - Backtrack, remove `3`: `sol = [1,2]`
   - Choose `3`: `sol = [1,3]`
     - Choose `2`: `sol = [1,3,2]` (Valid permutation, store in `res`)
     - Backtrack, remove `2`: `sol = [1,3]`
   - Backtrack, remove `3`: `sol = [1]`
   - Backtrack, remove `1`: `sol = []`

2. Choose `2`: `sol = [2]`
   - Choose `1`: `sol = [2,1]`
     - Choose `3`: `sol = [2,1,3]` (Valid permutation, store in `res`)
     - Backtrack, remove `3`: `sol = [2,1]`
   - Choose `3`: `sol = [2,3]`
     - Choose `1`: `sol = [2,3,1]` (Valid permutation, store in `res`)
     - Backtrack, remove `1`: `sol = [2,3]`
   - Backtrack, remove `3`: `sol = [2]`
   - Backtrack, remove `2`: `sol = []`

3. Choose `3`: `sol = [3]`
   - Choose `1`: `sol = [3,1]`
     - Choose `2`: `sol = [3,1,2]` (Valid permutation, store in `res`)
     - Backtrack, remove `2`: `sol = [3,1]`
   - Choose `2`: `sol = [3,2]`
     - Choose `1`: `sol = [3,2,1]` (Valid permutation, store in `res`)
     - Backtrack, remove `1`: `sol = [3,2]`
   - Backtrack, remove `2`: `sol = [3]`
   - Backtrack, remove `3`: `sol = []`

### Final Result:
```python
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

---

## Key Concepts Used
- **Backtracking**: We explore all possibilities recursively, making choices and undoing them when needed.
- **DFS (Depth-First Search)**: We traverse deeper into possible choices before backtracking.
- **List Copying (`sol[:]`)**: To store a snapshot of `sol` before it changes.

This method efficiently generates all permutations of `nums` by ensuring that we do not repeat numbers in a single permutation.

---

## Complexity Analysis
- **Time Complexity**: `O(N!)`, where `N` is the length of `nums`. This is because there are `N!` permutations.
- **Space Complexity**: `O(N!)` (storing results) + `O(N)` (recursion depth for backtracking).

---

## Summary
- Uses **backtracking** to explore all possible permutations.
- Avoids duplicate elements in a single permutation.
- Uses **DFS traversal** to explore possible solutions before backtracking.
- Generates all permutations and stores them in `res`.
- Works efficiently for small `N` but has factorial complexity.

This solution ensures that all **unique** permutations of the array are generated effectively.
