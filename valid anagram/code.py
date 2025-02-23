from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        

        s_dict=Counter(s)
        t_dict=Counter(t)
        if s_dict==t_dict:
            return True
        else:
            return False
