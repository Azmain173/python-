# LeetCode 78: Subsets

## Problem Statement
Given an array of **distinct integers**, return all possible **subsets (the power set)**. The solution must not contain duplicate subsets.

## Solution Explanation
The approach used in the solution is **backtracking**.

### **Code with Line-by-Line Explanation**
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)  # Get the length of the input list
        sol = []  # This will store the current subset being formed
        res = []  # This will store all the subsets
        
        def backtrack(i):
            if i == n:  # Base case: when index reaches the length of nums
                res.append(sol[:])  # Append a copy of sol to res
                return
            
            # Include nums[i] in the subset
            sol.append(nums[i])
            backtrack(i + 1)  # Recur for the next index
            
            # Exclude nums[i] from the subset (backtrack)
            sol.pop()
            backtrack(i + 1)  # Recur for the next index
        
        backtrack(0)  # Start recursion from index 0
        return res  # Return all generated subsets
```

### **Example Walkthrough**
#### Input:
```python
nums = [1, 2, 3]
```
#### Execution Steps:
- Start with an empty subset: `sol = []`
- Recursive tree for the function calls:

```
                                []
                           /           \
                       [1]              []
                      /    \           /    \
                [1,2]       [1]     [2]      []
               /    \       /  \    /  \     /  \
         [1,2,3]  [1,2]  [1,3] [1] [2,3] [2] [3] []
```

#### Output:
```python
[[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
```

### **Key Observations:**
1. We either **include** or **exclude** an element while forming subsets.
2. The recursive calls generate all possible combinations.
3. The base case ensures that once we reach the end of the list, we store the subset.

This method effectively finds all subsets in **O(2^N) time complexity**, where **N** is the length of `nums`.

### **Why Backtracking?**
Backtracking is used to explore all possibilities efficiently. The subset is formed by adding an element, then backtracking (removing it), and exploring further possibilities.

---
## **Alternative Iterative Approach**
If you prefer an iterative method:
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]  # Start with an empty subset
        
        for num in nums:
            res += [curr + [num] for curr in res]  # Generate new subsets by adding num
        
        return res
```
### **Output for `[1,2,3]`:**
```python
[[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
```

This is an **iterative** approach where we generate subsets by adding each number to existing subsets.

---
### **Conclusion**
- The **recursive backtracking** approach is intuitive and explores all possibilities.
- The **iterative approach** builds subsets incrementally.
- Both methods run in **O(2^N) time**, which is optimal for this problem.

