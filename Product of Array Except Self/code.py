class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        l_value=1
        r_value=1
        l_array=[0]*n
        r_array=[0]*n
        for i in range(n):
            j=-i-1
            l_array[i]=l_value
            r_array[j]=r_value
            l_value*=nums[i]
            r_value*=nums[j]
        return [l*r for l,r in zip(l_array,r_array)]
