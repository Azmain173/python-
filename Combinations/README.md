# LeetCode 77: Combinations

## Problem Statement
Given two integers `n` and `k`, return all possible combinations of `k` numbers chosen from the range `[1, n]`.

Example:
```
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
```

## Solution Breakdown

### Code:
```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol, res = [], []
        
        def backtrack(x):
            if len(sol) == k:
                res.append(sol[:])  # Base case: If combination size reaches k, add to result
                return
            
            left = x
            still_need = k - len(sol)  # Remaining elements needed
            
            if left > still_need:
                backtrack(x - 1)  # Skip the current number
            
            sol.append(x)  # Choose the current number
            backtrack(x - 1)  # Move to the next
            sol.pop()  # Undo the choice to explore other possibilities
        
        backtrack(n)
        return res
```

### Step-by-Step Execution (Example: `n=4, k=2`)

1. We start with an empty list `sol` to store the current combination and `res` to store all valid combinations.
2. The recursive `backtrack(x)` function is used to explore all possible selections from `n` down to `1`.
3. Base Case: When `len(sol) == k`, we store the current combination.
4. If there are still numbers available but we already have enough elements, we can skip the current number (`backtrack(x-1)`).
5. Otherwise, we include the current number `x` into `sol` and continue exploring (`backtrack(x-1)`).
6. After recursion, we remove the last added number to explore other possibilities (`sol.pop()`).

### Example Walkthrough for `n=4, k=2`:
```
backtrack(4)
    -> Choose 4 -> backtrack(3)
        -> Choose 3 -> [4,3] (Valid, add to res)
        -> Skip 3 -> backtrack(2)
            -> Choose 2 -> [4,2] (Valid, add to res)
            -> Skip 2 -> backtrack(1)
                -> Choose 1 -> [4,1] (Valid, add to res)
    -> Skip 4 -> backtrack(3)
        -> Choose 3 -> backtrack(2)
            -> Choose 2 -> [3,2] (Valid, add to res)
            -> Skip 2 -> backtrack(1)
                -> Choose 1 -> [3,1] (Valid, add to res)
        -> Skip 3 -> backtrack(2)
            -> Choose 2 -> backtrack(1)
                -> Choose 1 -> [2,1] (Valid, add to res)
```

### Final Output:
```
[[4,3], [4,2], [4,1], [3,2], [3,1], [2,1]]
```

### Complexity Analysis:
- The solution explores all possible ways to pick `k` elements from `n`, leading to a **time complexity of O(C(n, k))**, where `C(n, k) = n! / (k! * (n-k)!)`.
- The space complexity is **O(k)** for the recursion depth.

## Summary
- Uses **backtracking** to explore all combinations.
- Handles skipping numbers to optimize performance.
- Uses recursion with base cases to build valid combinations.

