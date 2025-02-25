# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low=1
        high=n
        while low<=high:
            mid=(low+high+1)//2
            if isBadVersion(mid)==0:
                low=mid+1
            else:
                high=mid-1
                
        return low
