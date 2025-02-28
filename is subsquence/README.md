# isSubsequence Function - Explanation

## Overview
This function checks whether a given string `s` is a subsequence of another string `t`. A subsequence means that the characters in `s` appear in `t` in the same order, but not necessarily consecutively.

## Code Implementation

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0  # Two pointers
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # If characters match, move the s pointer
                i += 1
            j += 1  # Always move the t pointer
        
        return i == len(s)  # If we matched all characters of s, return True
```

## Line-by-Line Explanation

### **Line 1:**
```python
class Solution:
```
- Defines a class named `Solution` which contains the function `isSubsequence`.
- This structure is commonly used in LeetCode problems.

### **Line 2:**
```python
    def isSubsequence(self, s: str, t: str) -> bool:
```
- Defines a method `isSubsequence` that takes two string arguments `s` (subsequence) and `t` (main string).
- The function returns a boolean (`True` or `False`).

### **Line 3:**
```python
        i, j = 0, 0  # Two pointers
```
- Initializes two pointers:
  - `i` (to track the position in `s`).
  - `j` (to track the position in `t`).
- Both start from index `0`.

### **Line 4-7:**
```python
        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # If characters match, move the s pointer
                i += 1
            j += 1  # Always move the t pointer
```
- A `while` loop runs as long as `i` has not reached the end of `s` and `j` has not reached the end of `t`.
- Inside the loop:
  - If `s[i]` matches `t[j]`, it means we found a valid subsequence character, so `i` moves to the next character in `s`.
  - `j` is always incremented, as we always scan through `t`.

### **Line 8:**
```python
        return i == len(s)  # If we matched all characters of s, return True
```
- After the loop, if `i` has reached the length of `s`, it means we have matched all characters of `s` in `t` in order, so we return `True`.
- Otherwise, return `False`.

## Example Runs

```python
sol = Solution()
print(sol.isSubsequence("abc", "ahbgdc"))  # True
print(sol.isSubsequence("axc", "ahbgdc"))  # False
print(sol.isSubsequence("", "ahbgdc"))     # True (empty string is always a subsequence)
print(sol.isSubsequence("abc", ""))        # False (s is not empty but t is empty)
```

## Complexity Analysis
- **Time Complexity:** `O(n)`, where `n` is the length of `t`. We iterate through `t` only once.
- **Space Complexity:** `O(1)`, as we use only two pointers and no extra data structures.

## Summary
- The function efficiently checks if `s` is a subsequence of `t` using a two-pointer technique.
- The solution runs in linear time and uses constant space.
- Works for edge cases like empty strings.

---

This README provides a detailed breakdown of the function to help understand its working and logic. 🚀

