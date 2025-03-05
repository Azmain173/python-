class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        sum=0
        min_length=float("inf")
        n=len(nums)
        for right in range(n):
            sum+=nums[right]
            while sum>=target:
                min_length=min(min_length,(right-left+1))
                sum-=nums[left]
                left+=1
        return min_length if min_length<float("inf") else 0
