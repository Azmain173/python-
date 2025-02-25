class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left=0
        right=n-1
        
        while left<=right:
            mid=(right+left+1)//2
            if target==nums[mid]:
                return mid
            elif nums[mid]<target:
                left=mid+1
                
            else:
                right=mid-1
           
        return -1
