# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def func(left,right):
            if left<=right:
                mid=(left+right)//2
                root=TreeNode(nums[mid])
                root.left=func(left,mid-1)
                root.right=func(mid+1,right)
                return root

        return func(0,len(nums)-1)

        """
        if not nums:
            return None

        n=len(nums)
        mid=n//2

        root=TreeNode(nums[mid])
        root.left=self.sortedArrayToBST(nums[:mid])
        root.right=self.sortedArrayToBST(nums[mid+1:])
        return root
        """
