# Remove K Digits - Leetcode 402 Solution

## Problem Statement
Given a non-negative integer `num` represented as a string and an integer `k`, remove `k` digits from the number so that the new number is the smallest possible.

### Example:
```
Input: num = "1432219", k = 3
Output: "1219"
```

---

## Key Concepts
- **Greedy Algorithm**: Always try to remove a digit that makes the number smaller.
- **Monotonic Stack**: Maintain an increasing stack to remove bigger digits on the left.
- **String Manipulation**: Avoid unnecessary conversions to integers.

---

## Final Code
```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for char in num:
            while stack and k > 0 and stack[-1] > char:
                stack.pop()
                k -= 1
            stack.append(char)

        # If still need to remove more digits, remove from the end
        stack = stack[:len(stack) - k]

        # Join stack into a string
        res = "".join(stack)

        # Remove leading zeros and return '0' if result is empty
        return res.lstrip('0') or "0"
```

---

## Code Explanation
### 1. `stack = []`
We initialize an empty stack to keep track of the digits that form the smallest number.

### 2. `for char in num:`
Loop through each digit in the string.

### 3. `while stack and k > 0 and stack[-1] > char:`
While the current digit is smaller than the last digit in the stack and we still have digits to remove (`k > 0`), pop from the stack.

### 4. `stack.append(char)`
Always add the current digit to the stack.

### 5. `stack = stack[:len(stack) - k]`
If some digits still need to be removed after the loop, remove them from the end.

### 6. `res = "".join(stack)`
Build the final number from the stack.

### 7. `return res.lstrip('0') or "0"`
Remove leading zeros. If nothing is left (empty string), return "0".

---

## Common Pitfalls
### ❌ Using `int()` to remove leading zeros:
```python
return str(int(res)) if res else "0"
```
- This works but may raise a `ValueError` for empty strings.

### ✅ Better Approach:
```python
return res.lstrip('0') or "0"
```
- Safe and clean string-based manipulation.

---

## Patterns Used
- **Monotonic Stack**: To maintain increasing order.
- **Greedy Removal**: Remove larger left-side digits when a smaller digit is found.
- **String Slicing**: For truncating leftover digits.
- **Edge Case Handling**: Empty results and leading zeros.

---

## Time and Space Complexity
- **Time Complexity**: O(n), where n is the length of the input string.
- **Space Complexity**: O(n), for the stack.

---

## Author
Azmain Abid Khan  
Feel free to connect with me on [LinkedIn](https://www.linkedin.com/) or check out more problems on my GitHub!
