class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        closest_sum=float('inf')
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=n-1
            while left<right:
                current_sum=nums[i]+nums[left]+nums[right]
                    
                if abs(target-current_sum)<abs(target-closest_sum):
                    closest_sum=current_sum

                if current_sum<target:
                    left+=1
                elif current_sum>target:
                    right-=1
                else:
                    return current_sum

        return closest_sum
