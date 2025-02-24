class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for c in operations:
            if c=='+':
                res.append(res[-1]+res[-2])
            elif c=='D':
                res.append(res[-1]*2)
            elif c=='C':
                res.pop()
            else:
                res.append(int(c))
        return sum(res)
