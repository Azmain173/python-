# Sum Root to Leaf Numbers (LeetCode 129)

## Problem Statement
Given the root of a binary tree containing digits from `0-9`, each root-to-leaf path represents a number. The task is to find the total sum of all root-to-leaf numbers.

A root-to-leaf path is defined as a path that starts from the root and ends at a leaf node. The value of the number is computed by concatenating the node values along the path.

### Example
**Input:**
```
    1
   / \
  2   3
```
**Output:** `25`

**Explanation:** The root-to-leaf numbers are `12` and `13`, so the total sum is `12 + 13 = 25`.

---

## Solution Approach

### Algorithm
1. Use Depth-First Search (DFS) to traverse the tree.
2. Maintain a running sum by multiplying the previous sum by `10` and adding the current node value.
3. When reaching a leaf node (both left and right children are `None`), return the computed sum.
4. Recursively call DFS on the left and right subtrees and return their sum.
5. If the tree is empty, return `0`.

### Code Implementation
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, sum):
            if not node:
                return 0
            sum = sum * 10 + node.val
            if not node.left and not node.right:
                return sum
            return dfs(node.left, sum) + dfs(node.right, sum)
        return dfs(root, 0)
```

---

## Complexity Analysis
- **Time Complexity:** `O(N)`, where `N` is the number of nodes in the tree. Each node is visited once.
- **Space Complexity:** `O(H)`, where `H` is the height of the tree (recursive call stack depth). In the worst case, `H = O(N)` for a skewed tree, and in the best case (balanced tree), `H = O(log N)`.

---

## Edge Cases Considered
- **Empty Tree:** If `root` is `None`, return `0`.
- **Single Node Tree:** The output should be the value of the single node.
- **Skewed Tree:** The function should correctly compute sums even if the tree is completely skewed (all left or all right children).

---

## Summary
This solution effectively computes the sum of root-to-leaf numbers using a DFS approach. It efficiently handles different types of binary trees while maintaining an optimal time complexity of `O(N)`. 🚀

