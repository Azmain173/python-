# Merge Two Binary Trees (Leetcode 617)

## Problem Statement
You are given two binary trees `root1` and `root2`. You need to merge the two trees by adding their corresponding node values. If a node exists in both trees, their values should be added together. If a node exists in only one tree, that node should be retained.

## Approach
The problem is solved using **recursion**. The key idea is:
- If `root1` is `None`, return `root2` (since there's nothing to merge).
- If `root2` is `None`, return `root1` (since there's nothing to merge).
- Otherwise, add the values of both nodes (`root1.val += root2.val`).
- Recursively merge the left and right subtrees.
- Return the updated `root1` as the merged tree.

## Code Implementation
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
```

## Example Walkthrough
### Example 1
#### Input:
```
Tree 1:         Tree 2:
    1              2
   / \            / \
  3   2          1   3
 /              \   \
5                4   7
```
#### Output:
```
Merged Tree:
    3
   / \
  4   5
 / \   \
5   4   7
```

## Complexity Analysis
- **Time Complexity**: O(N), where N is the minimum number of nodes in the two trees. Each node is visited once.
- **Space Complexity**: O(N) in the worst case due to recursive stack depth (if the tree is skewed).

## Edge Cases Considered
1. If `root1` is `None`, return `root2`.
2. If `root2` is `None`, return `root1`.
3. If both trees are empty, return `None`.
4. Uneven tree heights (one tree has more nodes than the other).

## Summary
This recursive solution efficiently merges two binary trees by adding their corresponding node values while maintaining the tree structure. It ensures that nodes present in only one tree are included in the merged output.

---
Let me know if you need further clarifications! 🚀

