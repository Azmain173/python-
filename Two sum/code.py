class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap={}
        for i,v in enumerate(numbers):
            diff=target-numbers[i]
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[v]=i
        return
               
