# Maximum Depth of a Binary Tree - Explanation

## Problem Statement
Given the root of a binary tree, return its maximum depth. The maximum depth is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

## Code Implementation
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)
```

## Line-by-Line Explanation

1. **Class Definition**
   ```python
   class Solution:
   ```
   - This defines the `Solution` class which contains the method `maxDepth`.

2. **Function Definition**
   ```python
   def maxDepth(self, root: Optional[TreeNode]) -> int:
   ```
   - This function takes a `TreeNode` object (`root`) as input and returns an integer representing the maximum depth of the tree.
   - `Optional[TreeNode]` means `root` can be `None` (an empty tree).

3. **Base Case (Stopping Condition)**
   ```python
   if not root:
       return 0
   ```
   - If `root` is `None`, the depth of the tree is `0`. This is the base case of the recursion.

4. **Recursive Calls**
   ```python
   left = self.maxDepth(root.left)
   right = self.maxDepth(root.right)
   ```
   - Recursively call `maxDepth` on `root.left` and `root.right` to find the depth of the left and right subtrees.
   - This continues until reaching the base case (when a node has no children).

5. **Return the Maximum Depth**
   ```python
   return 1 + max(left, right)
   ```
   - The depth of the current node is `1 + max(left, right)`, where:
     - `1` accounts for the current node.
     - `max(left, right)` ensures we take the longest path.

## Example Walkthrough

### Example 1
#### Input Tree:
```
       1
      / \
     2   3
    / \
   4   5
```
#### Recursive Calls:
```
maxDepth(1) → calls maxDepth(2) and maxDepth(3)
    maxDepth(2) → calls maxDepth(4) and maxDepth(5)
        maxDepth(4) → calls maxDepth(None) and maxDepth(None) → returns 0 → depth = 1
        maxDepth(5) → calls maxDepth(None) and maxDepth(None) → returns 0 → depth = 1
    maxDepth(2) → returns 1 + max(1,1) = 2
    maxDepth(3) → calls maxDepth(None) and maxDepth(None) → returns 1
maxDepth(1) → returns 1 + max(2,1) = 3
```
#### Final Output:
```python
Output: 3
```

### Example 2
#### Input Tree:
```
   1
  /
 2
```
#### Recursive Calls:
```
maxDepth(1) → calls maxDepth(2) and maxDepth(None)
    maxDepth(2) → calls maxDepth(None) and maxDepth(None) → returns 1
maxDepth(1) → returns 1 + max(1,0) = 2
```
#### Final Output:
```python
Output: 2
```

## Why Do We Use Recursion?
- **Natural Tree Traversal**: Trees are recursive structures, so recursion naturally fits.
- **Divides Problem into Subproblems**: Each node’s depth depends on its children.
- **Base Case Stops Infinite Calls**: Prevents unnecessary calculations.

## Complexity Analysis
- **Time Complexity**: O(N), where `N` is the number of nodes. Every node is visited once.
- **Space Complexity**: O(H), where `H` is the height of the tree due to recursion stack. In the worst case (skewed tree), O(N); in the best case (balanced tree), O(log N).

## Summary
- This function calculates the maximum depth of a binary tree using recursion.
- It traverses the tree and computes depth based on subtree heights.
- The solution runs in **O(N) time complexity** and has an **O(H) space complexity** due to recursion.

This method ensures efficient computation of the maximum depth of any binary tree structure. 🚀

