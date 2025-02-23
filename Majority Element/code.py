from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        n_dict=Counter(nums)
        for key in n_dict:
            if n_dict[key]>floor(n/2):
                return key
