### Diameter of a Binary Tree - README

#### Problem Statement:
The **diameter** of a binary tree is the **length of the longest path** between any two nodes in a tree. This path may or may not pass through the root. The length of a path is measured by the number of edges.

#### Code Explanation (Line by Line):

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
```
- The `TreeNode` class represents each node in a binary tree, having a `val` (value), `left` (left child), and `right` (right child).
- The `Solution` class contains the function `diameterOfBinaryTree` which calculates the tree's diameter.

```python
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
```
- The function `diameterOfBinaryTree` takes the root of a binary tree as input and returns the tree's diameter.
- `Optional[TreeNode]` indicates that the root can be a valid `TreeNode` or `None`.

```python
        largest_diameter = [0]  # global variable to store the maximum diameter found
```
- The `largest_diameter` is a **list** with a single element initialized to `0`.
- Lists are used instead of integers because integers are immutable in Python, and we need to update the diameter from a nested function.

```python
        def height(root):
```
- Defines a helper function `height` that computes the height of a node while updating the maximum diameter.

```python
            if not root:
                return 0
```
- If the `root` is `None`, return `0` since an empty subtree has a height of `0`.

```python
            left = height(root.left)
            right = height(root.right)
```
- Recursively calculate the height of the left and right subtrees.

```python
            diameter = left + right
```
- The **diameter** at a given node is the sum of the heights of its left and right subtrees.

```python
            largest_diameter[0] = max(largest_diameter[0], diameter)
```
- Updates `largest_diameter[0]` to store the **maximum** diameter found so far.

```python
            return 1 + max(left, right)
```
- Returns the **height** of the current node, which is `1 + max(left height, right height)`.

```python
        height(root)
```
- Calls the helper function on the root to calculate heights and update `largest_diameter`.

```python
        return largest_diameter[0]
```
- Returns the maximum diameter found in the tree.

#### Example Walkthrough:
##### Example 1:
**Input:**
```
       1
      / \
     2   3
    / \
   4   5
```
**Steps:**
- Height of node 4 = 1, height of node 5 = 1, so diameter at node 2 = `1 + 1 = 2`
- Height of node 3 = 1, diameter at node 1 = `2 + 1 = 3`
- The largest diameter found is **3**.

**Output:** `3`

#### Time Complexity:
- **O(N)** since we visit each node once.

#### Space Complexity:
- **O(N)** in the worst case (skewed tree) due to recursion stack depth.

This approach ensures an efficient computation of the diameter using a single pass (postorder traversal).

