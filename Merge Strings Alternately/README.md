# Merge Strings Alternately - README

## **Problem Statement**
Given two strings, merge them by alternating characters. If one string is longer, append the remaining characters at the end.

### **Example Inputs & Outputs**
```python
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
```

---

## **How the Code Works**

```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        i = j = 0
        merge = []  # Using a list to store characters efficiently

        while i < n1 and j < n2:  # Loop until one string is exhausted
            merge.append(word1[i])  # Append character from word1
            merge.append(word2[j])  # Append character from word2
            i += 1  # Move to next character in word1
            j += 1  # Move to next character in word2

        # Append remaining characters from the longer string
        merge.extend(word1[i:])  # Add leftover characters from word1
        merge.extend(word2[j:])  # Add leftover characters from word2

        return "".join(merge)  # Convert list to string and return
```

---

## **How Stack and List Are Used**
- **List (`merge`) as a Stack-like Structure**: 
  - We use a list to store characters dynamically.
  - Appending elements is an O(1) operation in Python.
  - Lists behave like stacks when using `append()`.
- **Converting List to String**:
  - `"".join(merge)` efficiently converts the list to a string.
  - Using `"+"` concatenation inside a loop would be inefficient.

---

## **Fixing Your Code's Problems**
### **Issues in Your Original Code**
❌ **Did not increment `i` and `j` inside the loop** → Leads to an infinite loop.  
❌ **Unnecessary `if-else` condition** → Adds redundant characters.  
❌ **Did not handle remaining characters** → Longer words would get truncated.  
❌ **Returned a list instead of a string** → Should convert list to string using `"".join(merge)`.  

### **Fixes Applied**
✅ **Incremented `i` and `j` properly** → Avoids infinite loops.  
✅ **Used a single loop to merge characters** → Removes redundant code.  
✅ **Handled leftover characters from longer strings**.  
✅ **Converted list to string using `join()`** → Efficient and correct output.  

---

## **Conclusion**
- Using **lists (as stacks)** allows efficient character merging.
- Converting the **list to a string using `"".join()`** avoids inefficiency.
- Properly incrementing indices and handling remaining characters ensures correctness.

This approach is both **optimized and easy to understand**! 🚀
