**Path Sum - LeetCode Problem Explanation**

## Problem Statement
Given the root of a binary tree and an integer `targetSum`, return `true` if the tree has a root-to-leaf path such that adding up all the values along the path equals `targetSum`. Otherwise, return `false`.

### Example
#### Example 1:
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The path 5 -> 4 -> 11 -> 2 adds up to 22.
```

#### Example 2:
```
Input: root = [1,2,3], targetSum = 5
Output: false
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
```
- The `Solution` class defines the `hasPathSum` function, which takes a binary tree (`root`) and an integer (`targetSum`) as input.
- The goal is to check if any root-to-leaf path sums to `targetSum`.

```python
        def sum(root,cur_sum):
```
- A helper function `sum` is defined within `hasPathSum` to perform recursion.
- It takes `root` (current node) and `cur_sum` (current sum of values along the path) as parameters.

```python
            if not root:
                return False
```
- If the current node is `None`, return `False` (Base case: if we reach a null node, no path exists).

```python
            cur_sum += root.val
```
- Add the value of the current node to `cur_sum`.

```python
            if not root.right and not root.left:
                return cur_sum == targetSum
```
- If the current node is a **leaf node** (has no left or right children), check if `cur_sum` equals `targetSum`.
- If `cur_sum == targetSum`, return `True`, meaning we found a valid path.
- Otherwise, return `False`.

```python
            return sum(root.left,cur_sum) or sum(root.right,cur_sum)
```
- Recursively call `sum` on the left and right children of the current node.
- If any of these recursive calls return `True`, propagate the result upwards.

```python
        return sum(root,0)
```
- The recursion is initially started with `cur_sum = 0`.
- If any path meets the condition, the function returns `True`; otherwise, `False`.

## Complexity Analysis
- **Time Complexity**: **O(N)**, where `N` is the number of nodes in the tree. We visit each node once.
- **Space Complexity**: **O(H)**, where `H` is the height of the tree (worst case O(N) for a skewed tree, best case O(logN) for a balanced tree).

## Summary
- The algorithm performs a **Depth-First Search (DFS)** traversal.
- It keeps track of the sum along each path and checks if a leaf node's sum matches `targetSum`.
- Uses **recursion** to explore both left and right subtrees.
- Returns `True` if any valid path is found; otherwise, `False`.

### Edge Cases Considered
1. **Empty tree (`root=None`)** → Should return `False`.
2. **Single node tree (`root=targetSum`)** → Should return `True` if root's value equals `targetSum`.
3. **Tree with negative values** → Ensures the algorithm works with negative numbers.
4. **Multiple valid paths** → Checks that at least one correct path is identified.

This solution effectively finds a root-to-leaf path with the desired sum using DFS. 🚀

