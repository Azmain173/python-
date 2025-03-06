# Subtree of Another Tree - README

## Problem Statement
Given the roots of two binary trees `root` and `subRoot`, determine whether `subRoot` is a subtree of `root`. A subtree of `root` is a tree consisting of a node in `root` and all of its descendants. The subtree must have the same structure and node values as `subRoot`.

## Example
**Input:**
```
root = [3,4,5,1,2], subRoot = [4,1,2]
```
**Output:**
```
true
```

## Code Breakdown

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
```
This defines the `isSubtree` function inside the `Solution` class, which takes two binary tree roots, `root` and `subRoot`.

```python
        def sameTree(p, q):
```
A helper function `sameTree` is defined to check if two trees are identical.

```python
            if not p and not q:
                return True
```
If both trees are empty (i.e., `None`), they are considered identical.

```python
            if (p and not q) or (q and not p):
                return False
```
If one of the trees is `None` while the other is not, they are not identical.

```python
            if p.val != q.val:
                return False
```
If the values of the current nodes in `p` and `q` do not match, they are not identical.

```python
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)
```
Recursively check if the left and right subtrees are identical.

```python
        def subTree(root):
```
A helper function `subTree` is defined to check if `subRoot` exists anywhere within `root`.

```python
            if not root:
                return False
```
If `root` is `None`, `subRoot` cannot be a subtree.

```python
            if sameTree(root, subRoot):
                return True
```
If the current `root` and `subRoot` are identical, return `True`.

```python
            return subTree(root.left) or subTree(root.right)
```
Recursively check if `subRoot` is a subtree of either the left or right child of `root`.

```python
        return subTree(root)
```
The function `isSubtree` starts by calling `subTree(root)`, initiating the search for `subRoot` in `root`.

## Complexity Analysis
- **Time Complexity:** O(N * M), where `N` is the number of nodes in `root` and `M` is the number of nodes in `subRoot`. In the worst case, for each node in `root`, we check if `subRoot` matches it, which takes `O(M)` time.
- **Space Complexity:** O(N) due to recursive stack space.

## Edge Cases Considered
1. `root` and `subRoot` are both `None` (returns `True`).
2. `subRoot` is `None` but `root` is not (returns `True`).
3. `root` is `None` but `subRoot` is not (returns `False`).
4. `subRoot` is a leaf node and exists in `root` (returns `True`).
5. `subRoot` is larger than `root` (returns `False`).

This ensures that all possible scenarios are covered in the solution.

