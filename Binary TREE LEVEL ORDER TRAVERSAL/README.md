**Binary Tree Level Order Traversal - README**

## Problem Statement
Given the root of a binary tree, return its level order traversal (i.e., values of the nodes at each level from left to right).

---
## Example
### Input:
```
    3
   / \
  9  20
    /  \
   15   7
```
### Output:
```
[
  [3],
  [9, 20],
  [15, 7]
]
```

---
## Code Breakdown

```python
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
```
- We import `deque` from `collections` for efficient queue operations.
- A class `TreeNode` is defined (commented out) to represent a node of the binary tree.
- The `levelOrder` function takes a `TreeNode` root as input and returns a list of lists containing values at each level.

```python
        if not root:
            return []
```
- If the tree is empty (`root` is `None`), return an empty list.

```python
        queue = deque()
        queue.append(root)
        ans = []
```
- Initialize a queue using `deque()`.
- Append the root node to the queue.
- Initialize an empty list `ans` to store the final level order traversal.

```python
        while queue:
            level = []
            n = len(queue)
```
- Continue the traversal until the queue is empty.
- Initialize `level` to store the current level’s values.
- `n = len(queue)` gives the number of nodes at the current level.

```python
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)
```
- Iterate `n` times (once for each node at the current level).
- Remove the front node from the queue.
- Add the node’s value to the `level` list.

```python
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
```
- If the node has a left child, add it to the queue.
- If the node has a right child, add it to the queue.

```python
            ans.append(level)
```
- Append the `level` list to `ans` after processing all nodes at the current level.

```python
        return ans
```
- Return the final result `ans`, containing values from each level.

---
## Complexity Analysis
- **Time Complexity:** O(N), where N is the number of nodes in the tree (each node is visited once).
- **Space Complexity:** O(N), as at most N/2 nodes can be stored in the queue at the last level.

---
## Edge Cases Considered
- Empty tree (`root = None`)
- Single-node tree
- Tree with only left or right children
- Balanced and unbalanced trees

