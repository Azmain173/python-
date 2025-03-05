# Checking If a Binary Tree is Balanced

## Problem Statement
A binary tree is considered **balanced** if the depth of the two subtrees of every node never differs by more than 1. Given the root of a binary tree, return `True` if the tree is balanced and `False` otherwise.

## Code Implementation
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]  # List used to store a single boolean value
        
        def height(root):
            if not root:
                return 0

            left = height(root.left)
            if balanced[0] is False:
                return 0  # Early termination if tree is already unbalanced

            right = height(root.right)
            if abs(left - right) > 1:
                balanced[0] = False  # Mark tree as unbalanced
                return 0

            return 1 + max(left, right)  # Return height of the current node
        
        height(root)  # Initiate recursive height check
        return balanced[0]  # Final balanced status
```

---

## Explanation of Each Line

### 1. **Class Definition**
```python
class Solution:
```
This defines the `Solution` class, which contains the `isBalanced` method.

### 2. **Using a List for a Mutable Boolean Value**
```python
balanced = [True]
```
- We use a **list** instead of a simple boolean variable because Python treats booleans as immutable inside nested functions. Lists, however, are mutable.
- `balanced[0]` initially holds `True`, meaning we assume the tree is balanced until proven otherwise.

### 3. **Recursive Height Function**
```python
def height(root):
```
- This function computes the height of a node while checking balance.
- It is **nested** within `isBalanced` so it can modify `balanced[0]`.

### 4. **Base Case (Stopping Condition)**
```python
if not root:
    return 0
```
- If the node is `None` (i.e., we reached a leaf), return height `0`.

### 5. **Recursive Calls to Compute Heights**
```python
left = height(root.left)
```
- Recursively calculate the **height** of the left subtree.
- If at any point `balanced[0]` becomes `False`, we stop further calculations.

### 6. **Early Termination for Efficiency**
```python
if balanced[0] is False:
    return 0
```
- If the tree is already determined to be unbalanced, stop further calculations.

### 7. **Compute Right Subtree Height**
```python
right = height(root.right)
```
- Recursively compute the height of the right subtree.

### 8. **Balance Condition Check**
```python
if abs(left - right) > 1:
    balanced[0] = False
    return 0
```
- If the **height difference** between left and right subtrees exceeds `1`, mark the tree as unbalanced.
- Return `0` to stop unnecessary calculations.

### 9. **Return Height of Current Node**
```python
return 1 + max(left, right)
```
- The height of a node is `1 + max(left, right)`, where:
  - `1` accounts for the current node.
  - `max(left, right)` ensures we use the taller subtree.

### 10. **Start Recursive Checks**
```python
height(root)
```
- Calls the `height` function to start the process from the root.

### 11. **Return Final Balance Status**
```python
return balanced[0]
```
- After all recursive calls, `balanced[0]` contains the final answer (`True` or `False`).

---

## Example Walkthrough

### Example 1: Balanced Tree
#### Input:
```
       1
      / \
     2   3
    / \   \
   4   5   6
```
#### Recursive Calls:
```
height(1) → calls height(2) and height(3)
    height(2) → calls height(4) and height(5)
        height(4) → returns 1
        height(5) → returns 1
    height(2) → returns 1 + max(1,1) = 2
    height(3) → calls height(None) and height(6)
        height(6) → returns 1
    height(3) → returns 1 + max(0,1) = 2
height(1) → returns 1 + max(2,2) = 3
```
#### Final Output:
```python
Output: True
```

### Example 2: Unbalanced Tree
#### Input:
```
       1
      /
     2
    /
   3
```
#### Recursive Calls:
```
height(1) → calls height(2) and height(None)
    height(2) → calls height(3) and height(None)
        height(3) → calls height(None) and height(None) → returns 1
    height(2) → returns 1 + max(1,0) = 2
height(1) → left = 2, right = 0 → abs(2-0) > 1 → unbalanced
```
#### Final Output:
```python
Output: False
```

---

## Complexity Analysis
- **Time Complexity**: O(N), where `N` is the number of nodes. Every node is visited once.
- **Space Complexity**: O(H), where `H` is the height of the tree. Worst case (skewed tree): O(N); Best case (balanced tree): O(log N).

## Summary
- This function checks whether a binary tree is balanced using a **recursive height function**.
- A **list is used** (`balanced[0]`) to track balance status.
- The function ensures **early termination** for efficiency.
- Runs in **O(N) time complexity** and **O(H) space complexity**.

This approach ensures an efficient and clear way to determine if a binary tree is balanced. ✅

