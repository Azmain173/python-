# Kth Smallest Element in a Binary Search Tree (BST)

## Problem Statement
Given the root of a binary search tree (BST) and an integer `k`, return the `k`th smallest element in the BST.

## Code Explanation
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=[k]  # A list to track how many elements we still need to visit before reaching the kth element
        ans=[0]    # A list to store the kth smallest element
        
        def dfs(node):
            if not node:
                return  # Base case: If the node is None, return
            
            dfs(node.left)  # Recursively traverse the left subtree (in-order traversal)
            
            if count[0] == 1:
                ans[0] = node.val  # Store the kth smallest value
            count[0] -= 1  # Decrease count after visiting a node
            
            if count[0] > 0:
                dfs(node.right)  # Recursively traverse the right subtree if needed
        
        dfs(root)  # Start in-order DFS traversal from the root
        return ans[0]  # Return the kth smallest element
```

## Step-by-Step Execution
1. **Initialize Variables:**
   - `count = [k]` is used to track how many nodes we need to visit before reaching the `k`th smallest.
   - `ans = [0]` will store the result.

2. **Define `dfs(node)`:**
   - If `node` is `None`, return (base case).
   - Recursively visit the left subtree first (`dfs(node.left)`).
   - When we reach the `k`th smallest node (`count[0] == 1`), store the node's value in `ans[0]`.
   - Decrease `count[0]` after visiting each node.
   - If `count[0] > 0`, continue the traversal to the right subtree (`dfs(node.right)`).

3. **Start Traversal:** Call `dfs(root)` to perform an **in-order traversal**, which visits nodes in sorted order.

4. **Return the Answer:** The `k`th smallest element is stored in `ans[0]`.

## Example Walkthrough
### Example 1:
**Input:**
```
     3
    / \
   1   4
    \
     2
```
`k = 1`

**In-order Traversal:** `[1, 2, 3, 4]`
- 1st smallest = **1**
- **Output:** `1`

### Example 2:
**Input:**
```
       5
      / \
     3   6
    / \
   2   4
  /
 1
```
`k = 3`

**In-order Traversal:** `[1, 2, 3, 4, 5, 6]`
- 3rd smallest = **3**
- **Output:** `3`

## Time and Space Complexity Analysis
- **Time Complexity:** `O(H + k)`, where `H` is the tree height.
  - In the worst case (`H = O(N)`, for a skewed tree), it is `O(N)`.
  - In a balanced BST, `H = O(log N)`, so it is `O(log N + k)`.
- **Space Complexity:** `O(H)`, due to recursive stack space.
  - Worst case: `O(N)` for a skewed tree.
  - Best case: `O(log N)` for a balanced BST.

## Edge Cases Considered
1. **Empty Tree:** If `root` is `None`, return 0 (not handled explicitly but assumed valid input).
2. **`k` is the smallest (`k=1`) or largest (`k=n`) element.**
3. **Tree is skewed (all nodes in a single branch).**
4. **Tree is balanced.**
5. **Duplicate values:** BSTs generally do not allow duplicates, but if allowed, the function still works.

## Summary
- This solution uses **in-order traversal** to find the `k`th smallest element efficiently.
- The **count variable** ensures we track the `k`th element correctly.
- **DFS recursion** is used to visit nodes in sorted order.

