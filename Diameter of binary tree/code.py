# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_diameter=[0]#global variable
        def height(root):
            if not root:
                return 0
            left=height(root.left)
            right=height(root.right)
            diameter=left+right
            largest_diameter[0]=max(largest_diameter[0],diameter)
            return 1+max(left,right)
        height(root)
        return largest_diameter[0]
