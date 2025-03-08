# README: Convert Sorted Array to Binary Search Tree (Leetcode 108)

## Problem Statement
Given an integer array `nums` where the elements are sorted in **ascending order**, convert it into a **height-balanced** binary search tree (BST).

A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differs by more than one.

## Approach
We use a **recursive divide-and-conquer** approach:
1. **Find the middle element** of the array and make it the root.
2. **Recursively construct the left subtree** from the left half of the array.
3. **Recursively construct the right subtree** from the right half of the array.
4. **Return the root** of the constructed BST.

---

## Code Implementation
### Approach 1: Using Explicit Left and Right Pointers
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def func(left, right):
            if left <= right:
                mid = (left + right) // 2
                root = TreeNode(nums[mid])
                root.left = func(left, mid - 1)
                root.right = func(mid + 1, right)
                return root
        
        return func(0, len(nums) - 1)
```
### Explanation
- The function `func(left, right)` is a helper function that constructs the BST recursively.
- The middle element `nums[mid]` is chosen as the root to ensure balance.
- The left half (`nums[left:mid]`) is used to construct the left subtree.
- The right half (`nums[mid+1:right]`) is used to construct the right subtree.
- Recursion stops when `left > right` (base case).

---

### Approach 2: Using List Slicing (Alternative Recursive Method)
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])  # Left half
        root.right = self.sortedArrayToBST(nums[mid+1:])  # Right half
        return root
```
### Explanation
- This version uses list slicing instead of explicit left and right indices.
- The middle element is chosen as the root.
- The left subtree is built from `nums[:mid]` (all elements before mid).
- The right subtree is built from `nums[mid+1:]` (all elements after mid).
- The function continues until the array is empty (base case).

---

## Complexity Analysis
- **Time Complexity:** O(N) since every element is visited once.
- **Space Complexity:**
  - **First Approach (explicit pointers):** O(log N) due to recursion depth.
  - **Second Approach (list slicing):** O(N) because slicing creates new arrays.

---

## Example Walkthrough
### Input:
```python
nums = [-10, -3, 0, 5, 9]
```
### Output (BST Representation):
```
      0
     / \
   -3   9
   /   /
 -10  5
```
### Explanation:
- The middle element `0` becomes the root.
- `-3` is chosen as the left child of `0`, and `9` as the right child.
- `-10` is chosen as the left child of `-3`, and `5` as the left child of `9`.
- The tree remains balanced.

---

## Conclusion
- Both approaches construct a height-balanced BST from a sorted array.
- The **first approach** is more memory-efficient (O(log N) vs. O(N)).
- The **second approach** is simpler but consumes more memory due to slicing.
- Use the first approach in coding interviews for better performance.

🚀 **Happy Coding!**

