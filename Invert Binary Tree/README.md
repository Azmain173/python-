# Invert Binary Tree - Code Explanation

## Problem Statement
Given the root of a binary tree, invert the tree (swap left and right children of all nodes) and return its root.

## Approach
This problem can be efficiently solved using a recursive approach where we swap the left and right child nodes at each level and then apply the same operation recursively on the left and right subtrees.

## Code
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:  # Base case: if the node is None, return None
            return None
        
        # Swap left and right subtrees
        root.left, root.right = root.right, root.left
        
        # Recursively invert left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root  # Return the modified tree
```

## Explanation (Line by Line)

### **Class Definition & Function Signature**
```python
from typing import Optional
```
- `Optional` is imported to indicate that `root` can be either a `TreeNode` or `None`.

```python
class Solution:
```
- Defines the class `Solution`, which contains the function `invertTree`.

```python
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
```
- Defines the function `invertTree` which takes a `TreeNode` (or `None`) as input and returns the root of the inverted tree.

### **Base Case: Handling Empty Nodes**
```python
        if not root:
            return None
```
- If `root` is `None` (i.e., the tree is empty or we reached a leaf node’s child), return `None`.

### **Swapping Left and Right Subtrees**
```python
        root.left, root.right = root.right, root.left
```
- The left and right children of the current node are swapped.

### **Recursive Calls: Inverting Subtrees**
```python
        self.invertTree(root.left)
```
- Calls `invertTree` on the left subtree (which was previously the right subtree before swapping).

```python
        self.invertTree(root.right)
```
- Calls `invertTree` on the right subtree (which was previously the left subtree before swapping).

**Why are these recursive calls needed?**
- Simply swapping the left and right children at the root level is not enough; we must apply the same swap operation at all levels of the tree.
- By recursively calling `invertTree` on both subtrees, we ensure that every node in the tree is processed and its children are swapped.

### **Returning the Modified Tree**
```python
        return root
```
- Returns the root of the modified tree after all inversions are complete.

## **Example Walkthrough**
### **Example 1**
#### **Input Tree:**
```
      4
     / \
    2   7
   / \  / \
  1   3 6  9
```

#### **Step-by-Step Execution:**
1. `root = 4`: Swap left and right (2 ↔ 7).
2. Call `invertTree(root.left)` on `7` (originally right subtree of `4`).
3. Call `invertTree(root.right)` on `2` (originally left subtree of `4`).
4. Continue swapping left and right for each subtree recursively.

#### **Output Tree:**
```
      4
     / \
    7   2
   / \  / \
  9   6 3  1
```

## **Time and Space Complexity**
### **Time Complexity: O(n)**
- Each node is visited once, making the time complexity **O(n)** where `n` is the number of nodes in the tree.

### **Space Complexity: O(h)**
- In the worst case (skewed tree), the recursion depth is equal to the height of the tree (`h`), making space complexity **O(h)**.
- In a balanced tree, `h ≈ log n`, so space complexity would be **O(log n)**.

## **Summary**
- **Base Case:** If `root` is `None`, return `None`.
- **Swap Children:** Swap `root.left` and `root.right`.
- **Recursive Calls:** Apply `invertTree` to `root.left` and `root.right`.
- **Return Root:** After inversion is applied to all levels.
- **Time Complexity:** `O(n)`, **Space Complexity:** `O(h)`.

This method ensures the entire tree is inverted efficiently using recursion. 🚀

