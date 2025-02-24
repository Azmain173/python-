from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon=Counter("balloon")
        counttext=Counter(text)
        res=float("inf")
        for c in balloon:
            res=min(res,counttext[c]//balloon[c])
        return res
