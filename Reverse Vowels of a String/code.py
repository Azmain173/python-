class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        n=len(s)
        l=0
        r=n-1
        vowels={"a","A","e","E","i","I","o","O","u","U"}
        while l<=r:
            if s[l] not in vowels:
                l+=1
            elif s[r] not in vowels:
                r-=1
            else:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
        return "".join(s)
