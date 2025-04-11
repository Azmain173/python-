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

## Questions Faced During Understanding

### ❓ User Question:
> "The `while` is inside a `for` loop — doesn’t that make the complexity `O(n^2)`?"

### ✅ Answer:
This is a very common and valid concern when seeing nested loops. However, in this case, **each element is pushed and popped at most once**, and although the `while` loop is inside a `for` loop, the total number of stack operations is still **O(n)**. The inner loop doesn’t run `n` times per iteration — it just helps merge values and the total work done across all iterations is bounded by `O(n)`.

---

## Optimized Solution Explanation
We use a **stack-based approach** to calculate the score.

- Push a `0` for every `(` to mark the beginning of a group.
- When we see a `)`, we pop the stack:
  - If the popped value is `0`, it means this was a simple `()` → push `1`
  - If it's a number, it means we’re closing a nested structure → pop again and push `2 * number`
- Instead of merging scores inside the loop with a `while`, we simply **sum the stack at the end** for clarity and performance.

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

## Code Walkthrough with Example
### Input: "(()(()))"
- Step-by-step stack behavior:
```
( → [0]
( → [0, 0]
) → pop 0 → push 1 → [0, 1]
( → [0, 1, 0]
( → [0, 1, 0, 0]
) → pop 0 → push 1 → [0, 1, 0, 1]
) → pop 1 → pop 0 → push 2 → [0, 1, 2]
) → pop 2 → pop 1 → push 2×2=4 → [0, 4]
Finally: sum([0, 4]) = 6
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
This looked like it might cause `O(n^2)` complexity, but it does not. Still, it’s cleaner to **avoid merging** and simply `sum(stack)` at the end.

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
- We clarified a common complexity concern.
- Instead of merging intermediate scores during the loop, we sum everything at the end.
- Clean, efficient, and easy to understand!

📌 Tip: This problem is a great example of converting recursive rules into iterative stack-based logic.

