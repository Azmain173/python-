# Generate Parentheses (LeetCode 22) - README

## Problem Statement
Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

### **Example 1:**
#### **Input:**
```python
n = 3
```
#### **Output:**
```python
["((()))","(()())","(())()","()(())","()()()"]
```

### **Example 2:**
#### **Input:**
```python
n = 1
```
#### **Output:**
```python
["()"]
```

---

## **Solution Explanation**

### **Approach: Backtracking**
- We maintain a list `sol` to build the current valid sequence of parentheses.
- We keep track of `open` and `close` counters to ensure well-formed parentheses.
- If `open < n`, we can add an opening `(`.
- If `close < open`, we can add a closing `)`.
- If `sol` has `2 * n` characters, we store the valid combination in `res`.

---

## **Code Explanation**

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, sol = [], []  # res stores the final result, sol builds valid parentheses
        
        def backtrack(open, close):
            if len(sol) == 2 * n:  # If we have used all n pairs
                res.append("".join(sol))  # Convert list to string and store
                return
            
            if open < n:  # Add '(' if we still have open brackets left
                sol.append("(")
                backtrack(open + 1, close)
                sol.pop()  # Backtrack to try other possibilities

            if open > close:  # Add ')' if we have more open than close
                sol.append(")")
                backtrack(open, close + 1)
                sol.pop()  # Backtrack to explore other paths
        
        backtrack(0, 0)  # Start with 0 open and 0 close
        return res  # Return the list of valid combinations
```

---

## **Example Walkthrough**
### **For `n = 3`:**
1. Start with `sol = []`, `open = 0`, `close = 0`.
2. Add `(` -> `sol = ['(']`, `open = 1`, `close = 0`.
3. Add `(` -> `sol = ['(', '(']`, `open = 2`, `close = 0`.
4. Add `(` -> `sol = ['(', '(', '(']`, `open = 3`, `close = 0`.
5. Add `)` -> `sol = ['(', '(', '(', ')']`, `open = 3`, `close = 1`.
6. Add `)` -> `sol = ['(', '(', '(', ')', ')']`, `open = 3`, `close = 2`.
7. Add `)` -> `sol = ['(', '(', '(', ')', ')', ')']`, `open = 3`, `close = 3`. Store the result.
8. Backtrack and try other possibilities.

### **Final Output for `n = 3`**
```python
["((()))","(()())","(())()","()(())","()()()"]
```

---

## **Time Complexity Analysis**
- Each valid sequence has length `2 * n`.
- The number of valid sequences follows the **Catalan number**: `C(n) = (1 / (n + 1)) * (2n choose n)`, which is approximately `O(4^n / sqrt(n))`.
- The space complexity is `O(2n)`, due to recursion depth and storing intermediate results.

---

## **Key Takeaways**
✅ Uses **backtracking** to explore all valid sequences.  
✅ Uses **two counters** (`open` and `close`) to ensure well-formed parentheses.  
✅ Efficient solution that avoids generating invalid cases.  

---

## **Similar Problems for Practice**
- **LeetCode 39**: [Combination Sum](https://leetcode.com/problems/combination-sum/)
- **LeetCode 40**: [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)
- **LeetCode 46**: [Permutations](https://leetcode.com/problems/permutations/)
- **LeetCode 47**: [Permutations II](https://leetcode.com/problems/permutations-ii/)
- **LeetCode 78**: [Subsets](https://leetcode.com/problems/subsets/)
