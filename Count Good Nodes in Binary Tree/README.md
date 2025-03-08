# README - Counting Good Nodes in a Binary Tree

## Problem Statement
Given a binary tree, a node is considered **"good"** if the path from the root to that node has no node with a greater value than the current node. We need to count the total number of good nodes in the tree.

## Approach
We use **Depth-First Search (DFS)** to traverse the tree while keeping track of the maximum value encountered along the path from the root. If a node's value is greater than or equal to this maximum value, it is considered a good node.

## Algorithm
1. **Start DFS from the root** with its own value as the initial `max_val`.
2. **Check if the node is good**:
   - If `node.val >= max_val`, count it as a good node.
3. **Update max_val** along the path.
4. **Recursively process left and right subtrees**, passing the updated `max_val`.
5. **Base case**: If `node is None`, return 0 (no nodes to count).

## Code Implementation
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_val):
            if not node:
                return 0  # Base case: no good nodes in a None subtree
            
            # Check if the current node is good
            good = 1 if node.val >= max_val else 0
            
            # Update max_val
            max_val = max(max_val, node.val)
            
            # Count good nodes in left and right subtrees
            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)
            
            return good
        
        return dfs(root, root.val)
```

## Explanation with Example
### Example Tree:
```
        3
       / \
      1   4
     /   / \
    3   1   5
```
### Execution Steps:
1. Start at `3`, it's good (since it's the root).
2. Move left to `1`: **not good** (smaller than `3`).
3. Move left to `3`: **good** (equal to `3`).
4. Move right to `4`: **good** (greater than `3`).
5. Move left to `1`: **not good** (smaller than `4`).
6. Move right to `5`: **good** (greater than `4`).
7. Total good nodes = **4**.

## Complexity Analysis
- **Time Complexity**: `O(N)`, where `N` is the number of nodes (we visit each node once).
- **Space Complexity**: `O(H)`, where `H` is the tree height (due to recursion stack).

## Edge Cases Considered
- **Single-node tree** → Always `1` good node.
- **All nodes with the same value** → Every node is good.
- **Skewed trees (only left or right children)** → Works the same as balanced trees.

## Summary
- We use **DFS with recursion**.
- Maintain a **max value along the path**.
- **Count nodes that meet the condition**.
- **Base case**: Return `0` for `None` nodes.
- **Final count** is returned as the total number of good nodes.

This approach ensures an efficient and correct solution to the problem. 🚀

