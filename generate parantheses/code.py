class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res,sol=[],[]
        def backtrack(open,close):
            if len(sol)==2*n:
                res.append("".join(sol))
                return
            
            if open<n:
                sol.append("(")
                backtrack(open+1,close)
                sol.pop()

            if open>close:
                sol.append(")")
                backtrack(open,close+1)
                sol.pop()
        backtrack(0,0)
        return res
