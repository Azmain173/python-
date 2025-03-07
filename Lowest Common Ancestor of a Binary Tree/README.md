# README - Understanding Lowest Common Ancestor (LCA) in a Binary Tree

## Overview
This document explains the **Lowest Common Ancestor (LCA) algorithm** using **recursion** in a binary tree. It includes code, step-by-step breakdowns, and answers to key questions regarding the recursive approach.

---

## **Code Explanation**

### **Python Code for Finding LCA**
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root  # If both left and right return a node, root is LCA
        else:
            return left or right  # Otherwise, return the non-null node
```

### **Algorithm Breakdown**
1. **Base Cases:**
   - If `root` is `None`, return `None`.
   - If `root` is equal to `p` or `q`, return `root` (because one of them is found).
2. **Recursive Search:**
   - Recursively call `lowestCommonAncestor` for the left and right subtrees.
   - Store the results in `left` and `right`.
3. **Finding the LCA:**
   - If both `left` and `right` are non-null, it means `p` and `q` are found in different subtrees, so `root` is the LCA.
   - Otherwise, return the non-null subtree (either `left` or `right`).

---

## **Example: Binary Tree**
Given the binary tree:
```
        3
       / \
      5   1
     / \  / \
    6   2 0  8
       / \
      7   4
```
Find the **LCA of `p=6` and `q=4`**.

### **Step-by-Step Recursive Calls**
| Step | Current Node | Left Subtree Result | Right Subtree Result | Returns |
|------|-------------|---------------------|----------------------|---------|
| 1    | `3`         | `LCA(5,6,4)`        | `LCA(1,6,4)`         | `5`     |
| 2    | `5`         | `LCA(6,6,4) → 6`    | `LCA(2,6,4) → 4`     | `5`     |
| 3    | `2`         | `LCA(7,6,4) → None` | `LCA(4,6,4) → 4`     | `4`     |
| 4    | `6`         | `None`              | `None`               | `6`     |

### **Backtracking Process**
- The function backtracks from **Node `2` to Node `5`**, carrying `4`.
- Node `5` receives `6` from the left and `4` from the right, confirming it as the LCA.

### **Final Answer:**
- The **Lowest Common Ancestor (LCA) of `6` and `4` is `5`**.

---

## **Key Questions and Answers**

### **Q1: What happens if `if left and right:` is True?**
- This means both `p` and `q` were found in separate subtrees.
- The current node is their Lowest Common Ancestor.

### **Q2: How does backtracking work from Node `2` to Node `5`?**
- When Node `2` finds `q=4`, it returns `4` to Node `5`.
- Node `6` is directly returned from the left subtree.
- Since both left and right returned non-null values, Node `5` is confirmed as the LCA.

### **Q3: Why does `left or right` return a single node?**
- If only one side contains `p` or `q`, we return that side as it contains the LCA.
- If `left` is `None`, it returns `right`, and vice versa.

---

## **Conclusion**
The **Lowest Common Ancestor (LCA) algorithm** follows a **depth-first search (DFS) approach**. It utilizes recursion to traverse the tree and **backtrack** when both `p` and `q` are found. The algorithm is efficient, running in **O(N) time complexity**, where `N` is the number of nodes in the tree.

