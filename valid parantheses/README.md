# Valid Parentheses - LeetCode Problem

## Problem Statement
Given a string `s` containing just the characters `'('`, `')'`, `'{', '}'`, `'['`, and `']'`, determine if the input string is **valid**.

A string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

### Example 1:
**Input:**
```python
s = "()"
```
**Output:**
```python
True
```

### Example 2:
**Input:**
```python
s = "()[]{}"
```
**Output:**
```python
True
```

### Example 3:
**Input:**
```python
s = "(]"
```
**Output:**
```python
False
```

### Example 4:
**Input:**
```python
s = "([)]"
```
**Output:**
```python
False
```

### Example 5:
**Input:**
```python
s = "{[]}"
```
**Output:**
```python
True
```

---

## Approach - Using Stack
### Steps:
1. Create a **stack** to keep track of opening brackets.
2. Create a **hashmap** that maps closing brackets to their corresponding opening brackets.
3. Iterate through each character in `s`:
   - If it’s a closing bracket, check if the stack is **not empty** and the top of the stack matches the expected opening bracket.
   - If they match, pop the stack; otherwise, return `False`.
   - If it’s an opening bracket, push it onto the stack.
4. At the end, if the stack is empty, return `True`; otherwise, return `False`.

---

## Code Implementation
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {')': '(', '}': '{', ']': '['}
        
        for c in s:
            if c in hashmap:
                if stack and stack[-1] == hashmap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return not stack
```

---

## Walkthrough Example
**Input:** `s = "({[]})"`

| Character | Stack | Action |
|-----------|----------------|----------------|
| `(`  | `[`(``]` | Push `(` |
| `{`  | `[(`, `{`]` | Push `{` |
| `[`  | `[(`, `{`, `[`]` | Push `[` |
| `]`  | `[(`, `{`]` | `]` matches `[`, so pop `[` |
| `}`  | `[(`]` | `}` matches `{`, so pop `{` |
| `)`  | `[]` | `)` matches `(`, so pop `(` |

- **Final Stack:** `[]` (empty ✅)
- **Output:** `True`

---

## Edge Cases
| Input | Expected Output | Explanation |
|--------|----------------|-------------|
| `""`  | `True` | Empty string is valid. |
| `"("` | `False` | No closing bracket. |
| `")("` | `False` | Wrong order. |
| `"([]{})"` | `True` | All match correctly. |
| `"({[)]}"` | `False` | Mismatched brackets. |

---

## Complexity Analysis
- **Time Complexity:** `O(n)` - Each character is processed once.
- **Space Complexity:** `O(n)` - Stack stores unmatched opening brackets in the worst case.

---

## Alternative Ways to Write the Last Line
The final return statement:
```python
return not stack
```
Can be written as:
1. **Using `len()` Function:**
    ```python
    return len(stack) == 0
    ```
2. **Using an Explicit If-Else Statement:**
    ```python
    if not stack:
        return True
    else:
        return False
    ```
3. **Using a Ternary Operator:**
    ```python
    return True if len(stack) == 0 else False
    ```

---

## Summary
✔ **Use a stack** to track unmatched opening brackets.  
✔ **Use a dictionary (`hashmap`)** to match closing brackets with their corresponding opening brackets.  
✔ **Check the stack top before popping** to prevent errors.  
✔ **At the end, the stack must be empty** for the string to be valid.  

This problem is a great example of how **stacks** can be used for parsing and validation problems! 🚀
