# Leetcode 856: Score of Parentheses

## Problem Description
Given a balanced parentheses string `s`, compute the **score** of the string based on the following rules:

1. `"()"` has score `1`
2. `"AB"` has score `A + B`, where A and B are balanced parentheses strings
3. `"(A)"` has score `2 * A`, where A is a balanced parentheses string

### Example:
```
Input: "(()(()))"
Output: 6
```

---

## Solution Explanation
We use a **stack-based approach** to calculate the score.

- Push a `0` for every `(` to mark the beginning of a group.
- When we see a `)`, we pop the stack:
  - If the popped value is `0`, it means this was a simple `()` → push `1`
  - If it's a number, it means we’re closing a nested structure → pop again and push `2 * number`
- At the end, **sum all the elements in the stack** to get the total score.

---

## Code: Clean Stack-Based Solution
```python
# File: score_of_parentheses.py

def scoreOfParentheses(s: str) -> int:
    stack = []

    for char in s:
        if char == '(':
            stack.append(0)
        else:
            val = stack.pop()
            if val == 0:
                stack.append(1)
            else:
                stack.pop()  # Remove the matching 0
                stack.append(2 * val)

    return sum(stack)
```

---

## Time and Space Complexity
- **Time Complexity:** `O(n)`
  - We loop through the string once.
  - Each element is pushed and popped from the stack at most once.

- **Space Complexity:** `O(n)`
  - In the worst case (fully nested structure), the stack can grow to length `n`.

---

## Optimization Note
Earlier versions of this code merged scores inside the loop using a `while` loop:
```python
while len(stack) >= 2 and stack[-1] != 0 and stack[-2] != 0:
    stack.append(stack.pop() + stack.pop())
```
This is unnecessary. Instead, we use `sum(stack)` at the end for a cleaner, more efficient solution.

---

## Sample Inputs and Outputs
```python
assert scoreOfParentheses("()") == 1
assert scoreOfParentheses("(())") == 2
assert scoreOfParentheses("()()") == 2
assert scoreOfParentheses("(()(()))") == 6
```

---

## Summary
- We used a stack to keep track of structure.
- Instead of merging intermediate scores during the loop, we sum everything at the end.
- Clean, efficient, and easy to understand!

📌 Tip: This problem is a great example of converting recursive rules into iterative stack-based logic.

