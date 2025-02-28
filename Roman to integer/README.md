# Roman to Integer - README

## Problem Statement
The problem is to convert a given Roman numeral string (e.g., "IX", "MCMXCIV") into an integer. Roman numerals follow specific subtraction rules, such as:
- **IV = 4** (5 - 1)
- **IX = 9** (10 - 1)
- **XL = 40** (50 - 10)
- **CM = 900** (1000 - 100)

Our goal is to implement a function that efficiently converts a Roman numeral string into an integer.

---

## Implementation
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}  # Mapping Roman numerals to integers
        
        i = sum = 0  # Initialize index and sum to 0
        n = len(s)   # Get the length of the input string
        
        while i < n:  # Iterate through the string
            if i < n-1 and d[s[i]] < d[s[i+1]]:  # Check if subtraction is needed
                sum += d[s[i+1]] - d[s[i]]  # Subtract smaller value from larger one
                i += 2  # Skip the next character since it's already used
            else:
                sum += d[s[i]]  # Otherwise, just add the current numeral
                i += 1  # Move to the next character
        
        return sum  # Return the final integer value
```

---

## Example Runs
```python
sol = Solution()
print(sol.romanToInt("III"))   # Output: 3
print(sol.romanToInt("IV"))    # Output: 4
print(sol.romanToInt("IX"))    # Output: 9
print(sol.romanToInt("LVIII")) # Output: 58
print(sol.romanToInt("MCMXCIV")) # Output: 1994
```

---

## Why `while` Instead of `for`?
Initially, using `for i in range(n):` seems like a good approach, but it **fails for subtraction cases** like "IX" or "CM".

### Why?
- The `for` loop **automatically increments `i`** in each iteration.
- If we detect a subtraction case (`d[s[i]] < d[s[i+1]]`), we need to **skip the next character** (`i += 2`).
- But since `for` loops control `i` automatically, our manual `i += 2` gets **overwritten**, skipping characters incorrectly.

### Example of Failure with `for` Loop:
```python
for i in range(n):
    if i < n-1 and d[s[i]] < d[s[i+1]]:
        sum += d[s[i+1]] - d[s[i]]
        i += 1  # This doesn't prevent `i` from being incremented again
    else:
        sum += d[s[i]]
```

#### Issue:
For "IX":
- `i = 0`: Recognizes `I < X`, adds `9`, and **tries to skip `X` (`i += 1`)**.
- But `for` loop **also** increments `i`, making `i = 2`, **skipping characters incorrectly**.

### Solution: Use `while`
- `while` allows **manual control** over `i`, ensuring correct character skipping (`i += 2`).
- `for` is better for fixed iteration, but not when we need to **dynamically skip characters**.

---

## Summary
- ✅ **Correct approach:** `while i < n:` (allows skipping characters manually)
- ❌ **Incorrect approach:** `for i in range(n):` (automatically increments `i`, causing errors)

Using `while` ensures that we correctly parse the Roman numeral while handling special subtraction cases efficiently.
