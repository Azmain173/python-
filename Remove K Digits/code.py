class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        
        for char in num:
            while stack and k>0 and stack[-1]>char:
                stack.pop()
                k-=1
            stack.append(char)

        #increasing order
        stack=stack[:len(stack)-k]
        #list->string
        res="".join(stack)
        #for leading zeros
        #return str(int(res)) if res else "0"
        return res.lstrip('0') or "0"
