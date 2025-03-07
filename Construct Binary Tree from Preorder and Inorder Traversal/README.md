# Constructing a Binary Tree from Preorder and Inorder Traversals

## Overview
This document explains how to reconstruct a binary tree from its **preorder** and **inorder** traversal lists using Python. It details how the algorithm works, step-by-step, and clarifies how nodes are selected and assigned correctly without reuse.

## Understanding Preorder and Inorder Traversals

- **Preorder Traversal (Root → Left → Right)**: The first element is always the root of the tree.
- **Inorder Traversal (Left → Root → Right)**: The root is found between the left and right subtree elements.

Using these two traversals together allows us to uniquely reconstruct the binary tree.

## Python Implementation
### TreeNode Class
```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

### Solution Class
```python
from typing import List, Optional

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # Root is the first element of preorder traversal
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        
        # Find the root index in inorder traversal
        inorder_index = inorder.index(root_val)
        
        # Recursively build the left and right subtrees
        root.left = self.buildTree(preorder, inorder[:inorder_index])
        root.right = self.buildTree(preorder, inorder[inorder_index+1:])
        
        return root
```

## Step-by-Step Execution Example
**Input:**
```python
preorder = [3, 9, 20, 15, 7]
inorder  = [9, 3, 15, 20, 7]
```

**Step 1: Selecting Root**
- The first element in `preorder` is `3` (root).
- Locate `3` in `inorder`:
  ```
  inorder = [9, 3, 15, 20, 7]
                  ^ (index 1)
  ```
- Left subtree: `[9]`  
- Right subtree: `[15, 20, 7]`

**Step 2: Constructing Left Subtree (`9`)**
- Next `preorder.pop(0) → 9`.
- Find `9` in `inorder`:
  ```
  inorder = [9]
          ^ (index 0)
  ```
- Left subtree: `[]` (returns `None`)
- Right subtree: `[]` (returns `None`)

✔️ Node `9` is a **leaf node**.

**Step 3: Constructing Right Subtree (`20`)**
- Next `preorder.pop(0) → 20`.
- Find `20` in `inorder`:
  ```
  inorder = [15, 20, 7]
                 ^ (index 1)
  ```
- Left subtree: `[15]`
- Right subtree: `[7]`

**Step 4: Recursively Build Remaining Nodes (`15` and `7`)**
- `preorder.pop(0) → 15` (left of `20`).
- `preorder.pop(0) → 7` (right of `20`).

**Final Tree Structure:**
```
        3
       / \
      9   20
         /  \
        15   7
```

## How It Ensures Nodes Are Not Reused
### **Preorder Ensures Unique Root Selection**
- `preorder.pop(0)` always picks the **next unused node** as the root.

### **Inorder Ensures Correct Left-Right Structure**
- The `inorder` list is **sliced at the root index**, so left and right subtrees get separate portions.
- Recursive calls **never see out-of-scope nodes**.

**Example:** When building `9`, it only sees `inorder = [9]`, not `3` or `20`.

## Conclusion
✅ The algorithm correctly constructs the binary tree using preorder and inorder traversal.
✅ It ensures no node is reused and preserves the left-right structure.
✅ Recursion naturally divides and assigns subtrees correctly.

---
**This method guarantees unique and correct tree reconstruction! 🚀**

