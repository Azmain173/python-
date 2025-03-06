## Symmetric Tree - LeetCode Problem

### Problem Statement:
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

### Understanding the Code:

#### Code:
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def same(root1, root2):
            if not root1 and not root2:
                return True
            if (root1 and not root2) or (root2 and not root1):
                return False
            if root1.val != root2.val:
                return False
            return same(root1.left, root2.right) and same(root1.right, root2.left)
        return same(root, root)
```

### Explanation:

1. **Base Case:**
   - The function `same(root1, root2)` is a helper function that checks if two trees are mirror images of each other.
   - If both `root1` and `root2` are `None`, it means they are symmetric, so return `True`.

2. **Asymmetry Detection:**
   - If one of `root1` or `root2` is `None` while the other is not, return `False` because the structure is not symmetric.
   - If the values of `root1` and `root2` do not match, return `False` because the trees are not mirror images.

3. **Recursive Check for Symmetry:**
   - The function checks if the left subtree of `root1` is a mirror of the right subtree of `root2` and vice versa.
   - `same(root1.left, root2.right)`: Ensures the left subtree of one tree matches the right subtree of the other.
   - `same(root1.right, root2.left)`: Ensures the right subtree of one tree matches the left subtree of the other.

4. **Final Return Statement:**
   - The function `isSymmetric` calls `same(root, root)` to check if the entire tree is symmetric.

### Example Walkthrough:

#### Example 1:
```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```
- The left subtree (2 → 3, 4) is a mirror of the right subtree (2 → 4, 3), so the tree is symmetric.
- Output: `True`

#### Example 2:
```
    1
   / \
  2   2
   \    \
   3     3
```
- The left subtree (2 → None, 3) is NOT a mirror of the right subtree (2 → None, 3), so the tree is not symmetric.
- Output: `False`

### Time Complexity:
- Each node is visited once, and we perform constant-time comparisons.
- **Time Complexity: O(N)**, where N is the number of nodes in the tree.

### Space Complexity:
- In the worst case (skewed tree), the recursion stack can go up to O(N).
- **Space Complexity: O(H)**, where H is the height of the tree (log N for balanced trees, N for skewed trees).

### Summary:
- The function checks if the tree is symmetric by comparing left and right subtrees recursively.
- It ensures that nodes are mirrored correctly at each level.
- Efficient and uses recursion to solve the problem in **O(N) time and O(H) space**.

