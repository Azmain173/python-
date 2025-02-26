class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right=mid
        min_index=left


        
        if min_index==0:
            left,right=0,n-1
        elif target>=nums[0] and target<=nums[min_index-1]:
            left,right=0,min_index-1
        else:
            left,right=min_index,n-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                return mid
        return -1
