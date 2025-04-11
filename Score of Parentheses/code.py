class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        for char in s:
            if char=="(":
                stack.append(0)
            elif char==")":
                val=stack.pop()
                if val==0:
                    stack.append(1)
                else:
                    stack.pop()
                    stack.append(val*2)
            
            while len(stack)>=2 and stack[-1]!=0 and stack[-2]!=0:
                stack.append(stack.pop()+stack.pop())
        return stack[0]
