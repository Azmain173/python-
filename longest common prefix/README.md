# Longest Common Prefix (LeetCode Problem #14)

This repository contains a Python solution to the **LeetCode Problem #14 - Longest Common Prefix**. The task is to find the longest common prefix string among an array of strings. If no common prefix exists, return an empty string.

---

## Problem Description

Given an array of strings `strs`, find the longest common prefix that is shared by all the strings.

### Example Inputs and Outputs:
- **Input:** `["flower", "flow", "flight"]`  
  **Output:** `"fl"`  
- **Input:** `["dog", "racecar", "car"]`  
  **Output:** `""` (no common prefix)  

---

## Approach and Solution

The solution compares each string character by character, up to the length of the shortest string in the array, and returns the longest prefix that matches in all strings.

### Code:
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = float("inf")
        for s in strs:
            if len(s) < min_length:
                min_length = len(s)

        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i += 1

        return s[:i]
```

---

## Explanation

### Step-by-Step Breakdown:
1. **Find the Length of the Shortest String:**
   - Iterate through all the strings and store the length of the shortest one in `min_length`. This is because the longest possible common prefix cannot be longer than the shortest string.

2. **Character Comparison:**
   - Use a `while` loop to compare characters at each position `i` from all strings in the array.
   - If any character at position `i` in a string `s` does not match the character at the same position in the first string (`strs[0][i]`), return the common prefix up to that index.

3. **Increment and Return:**
   - If all characters match up to `min_length`, return the entire prefix up to `i`.

---

## Time and Space Complexity
- **Time Complexity:** O(N * min_length), where N is the number of strings and `min_length` is the length of the shortest string.
- **Space Complexity:** O(1), since the solution uses a constant amount of extra space.

---

## Example Walkthrough
For `strs = ["flower", "flow", "flight"]`:
- The shortest string is "flow" (length 4).
- Compare the characters:
  - `i = 0`: All strings have `'f'` → Continue.
  - `i = 1`: All strings have `'l'` → Continue.
  - `i = 2`: "flower" and "flow" have `'o'`, but "flight" has `'i'` → Mismatch! Return `"fl"`.

---

## Conclusion
This solution efficiently finds the longest common prefix by leveraging character-by-character comparisons and limiting the checks to the shortest string length. It works well even for edge cases, like when the input array contains empty strings or completely different strings.

---

## Author
Azmain Abid Khan
