class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        sum=0
      
        for i in range(0,k):
            sum=sum+nums[i]
            
        max_average=sum/k
        for i in range(k,n):
            sum=sum+nums[i]
            sum=sum-nums[i-k]
            avg2=sum/k
            max_average=max(max_average,avg2)
        return max_average
