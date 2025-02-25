class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s=s.lower()
        filtered_str = "".join([ch for ch in s if ch.isalnum()])
        left=0
        n=len(filtered_str)
        right=n-1
        while left<right:
            if filtered_str[left]!=filtered_str[right]:
                return False
            left+=1
            right-=1
        return True
        
