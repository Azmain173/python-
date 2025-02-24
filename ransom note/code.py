from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic=Counter(magazine)
        for c in ransomNote:
            if c not in dic:
                return False
            elif dic[c]==1:
                del dic[c]
            else:
                dic[c]-=1
        return True
