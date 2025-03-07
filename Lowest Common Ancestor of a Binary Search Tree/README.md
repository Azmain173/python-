# Lowest Common Ancestor of a Binary Search Tree

## Problem Statement
Given a **Binary Search Tree (BST)** and two nodes `p` and `q`, find their **Lowest Common Ancestor (LCA)**. The LCA of two nodes is defined as the lowest node in the tree that has both `p` and `q` as descendants.

## Code Explanation

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left  # Both nodes are in the left subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right  # Both nodes are in the right subtree
            else:
                return root  # Found the split point where p and q diverge
        return None  # If not found
```

## Step-by-Step Execution
1. **Initialize Traversal**
   - Start from the root node.

2. **Check Relationship Between `p`, `q`, and `root`**
   - If both `p` and `q` are **smaller** than `root.val`, move left (`root = root.left`).
   - If both `p` and `q` are **greater** than `root.val`, move right (`root = root.right`).
   - If `p` and `q` are on **different sides** of `root`, `root` is their **LCA**.

3. **Return the LCA**
   - If `root` is `None`, return `None` (edge case where the BST is empty).
   - Otherwise, return the node where `p` and `q` diverge.

## Example Walkthrough
### Example 1
#### Input BST:
```
        6
       / \
      2   8
     / \ / \
    0  4 7 9
      / \ 
     3   5
```
#### Given Nodes:
`p = 2`, `q = 8`

#### Execution:
1. Start at `root = 6`.
2. Since `p = 2` is **less** than `6` and `q = 8` is **greater** than `6`, we find the **LCA at 6**.

#### Output:
`LCA = 6`

### Example 2
#### Given Nodes:
`p = 2`, `q = 4`

#### Execution:
1. Start at `root = 6`, both `p = 2` and `q = 4` are **less** than `6`, so move left to `root = 2`.
2. At `root = 2`, `p = 2` and `q = 4` are on **different sides** (one is `root`, the other in its subtree).

#### Output:
`LCA = 2`

## Complexity Analysis
- **Time Complexity:** `O(h)`, where `h` is the height of the BST (logarithmic in a balanced BST, linear in a skewed BST).
- **Space Complexity:** `O(1)`, since we use a constant amount of space (iterative approach, no recursion stack).

## Edge Cases Considered
- If `p` or `q` does not exist in the BST.
- If `p == q`, then `p` (or `q`) itself is the LCA.
- If `p` and `q` are both direct children of the root, root becomes the LCA.

## Summary
- The algorithm efficiently finds the LCA in a BST by leveraging BST properties.
- It follows an **iterative approach**, avoiding recursion overhead.
- The function returns the first node where `p` and `q` split into different subtrees, which is the **LCA**.

Let me know if you have any questions! 🚀
