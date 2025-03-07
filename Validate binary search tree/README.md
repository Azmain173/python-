# Validate Binary Search Tree (BST)

## Problem Statement
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A **BST** must satisfy the following conditions:
1. The left subtree of a node contains only nodes with values **less than** the node's value.
2. The right subtree of a node contains only nodes with values **greater than** the node's value.
3. Both the left and right subtrees must also be **binary search trees**.

## Code Explanation
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, min, max):
            if not node:
                return True
            if node.val <= min or node.val >= max:
                return False
            return valid(node.left, min, node.val) and valid(node.right, node.val, max)
        return valid(root, float("-inf"), float("inf"))
```

### Line-by-Line Breakdown

1. **Defining the function**
   ```python
   def isValidBST(self, root: Optional[TreeNode]) -> bool:
   ```
   - The function `isValidBST` takes the `root` of the tree as input.
   - It returns `True` if the tree is a valid BST, otherwise `False`.

2. **Helper Function: `valid`**
   ```python
   def valid(node, min, max):
   ```
   - This helper function **recursively** checks whether the subtree rooted at `node` satisfies the BST property.
   - The `min` and `max` parameters define the valid range for node values.

3. **Base Case: If `node` is None**
   ```python
   if not node:
       return True
   ```
   - If we reach a `None` node, return `True` (empty subtrees are valid BSTs).

4. **Check if the node violates the BST property**
   ```python
   if node.val <= min or node.val >= max:
       return False
   ```
   - If `node.val` is **not within** the `(min, max)` range, return `False`.

5. **Recursive Calls for Left and Right Subtrees**
   ```python
   return valid(node.left, min, node.val) and valid(node.right, node.val, max)
   ```
   - Recursively validate the **left subtree**, ensuring all nodes are `< node.val`.
   - Recursively validate the **right subtree**, ensuring all nodes are `> node.val`.
   - Both must be `True` for the tree to be a valid BST.

6. **Initial Call to `valid`**
   ```python
   return valid(root, float("-inf"), float("inf"))
   ```
   - The BST starts with the entire integer range (`-∞` to `+∞`).
   - The root can take any value, but its left and right children must adhere to BST rules.

## Example Walkthrough
### Example 1:
#### Input:
```
    2
   / \
  1   3
```
#### Function Call:
```python
isValidBST(root)
```
- The root value `2` is between `-∞` and `+∞` (valid).
- The left child `1` is in range `(-∞, 2)` (valid).
- The right child `3` is in range `(2, +∞)` (valid).
- The tree satisfies BST properties → **returns `True`**.

### Example 2 (Invalid BST):
#### Input:
```
    5
   / \
  1   4
     / \
    3   6
```
#### Function Call:
```python
isValidBST(root)
```
- The root `5` is valid.
- The left child `1` is valid.
- The right child `4` **violates** the BST rule because `4 < 5`, but has a left child `3`, which should be greater than `5`.
- The function returns `False`.

## Complexity Analysis
- **Time Complexity:** O(N), where N is the number of nodes.
  - Each node is visited once.
- **Space Complexity:** O(H), where H is the height of the tree.
  - In the worst case (skewed tree), the recursion depth is O(N).
  - In the best case (balanced tree), the recursion depth is O(log N).

## Summary
- This solution uses **recursion** to validate the BST properties efficiently.
- The `min` and `max` bounds ensure correctness.
- The **time complexity is O(N)**, making it optimal for checking BST validity.

Let me know if you need further clarifications!

