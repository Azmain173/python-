# Maximum Number of Balloons - LeetCode Solution

## Problem Statement
You are given a string `text`. Your task is to determine how many times you can form the word **"balloon"** using the letters in `text`.

### Example 1:
#### **Input:**
```plaintext
text = "loonbalxballpoon"
```
#### **Output:**
```plaintext
2
```

### Example 2:
#### **Input:**
```plaintext
text = "leetcode"
```
#### **Output:**
```plaintext
0
```

---

## Understanding the Problem
- The word **"balloon"** consists of specific letters:
  - `'b'` → appears **1** time
  - `'a'` → appears **1** time
  - `'l'` → appears **2** times
  - `'o'` → appears **2** times
  - `'n'` → appears **1** time
- We need to check how many full "balloon" words can be formed from the given `text`.

---

## **Approach: Using Hash Map (Counter)**
### **Step 1: Count Letter Frequencies**
- Use `Counter` from the `collections` module to count letter occurrences in both `text` and "balloon".

### **Step 2: Find the Maximum Possible Words**
- Check the availability of each letter in "balloon".
- Compute the maximum number of times we can use each letter to form "balloon":
  
  ```plaintext
  max_possible = count_in_text[letter] // count_in_balloon[letter]
  ```
- Since all letters are needed, the final answer is the **minimum** of these values (bottleneck principle).

---

## **Implementation**
```python
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = Counter("balloon")  # {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
        counttext = Counter(text)  # Count letters in given text
        
        res = float("inf")  # Initialize result to a large number
        
        for c in balloon:  # Iterate over required characters
            res = min(res, counttext[c] // balloon[c])  # Find the limiting factor
        
        return res  # Return the minimum possible "balloon" count
```

---

## **Example Walkthrough**
### Example 1: `text = "loonbalxballpoon"`
```plaintext
Letter Counts in text: {'l': 4, 'o': 4, 'n': 2, 'b': 2, 'a': 2}
Letter Requirements:   {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
```

| Letter | Needed (from "balloon") | Available (from `text`) | Max possible (`Available // Needed`) |
|--------|-------------------------|-----------------------|--------------------------------|
| `'b'`  | 1                       | 2                     | `2 // 1 = 2`                 |
| `'a'`  | 1                       | 2                     | `2 // 1 = 2`                 |
| `'l'`  | 2                       | 4                     | `4 // 2 = 2`                 |
| `'o'`  | 2                       | 4                     | `4 // 2 = 2`                 |
| `'n'`  | 1                       | 2                     | `2 // 1 = 2`                 |

✅ **Final Answer:** `min(2, 2, 2, 2, 2) = 2`

### Example 2: `text = "balon"`
```plaintext
Letter Counts in text: {'b': 1, 'a': 1, 'l': 1, 'o': 1, 'n': 1}
```
| Letter | Needed | Available | Max possible |
|--------|--------|-----------|--------------|
| `'b'`  | 1      | 1         | `1 // 1 = 1` |
| `'a'`  | 1      | 1         | `1 // 1 = 1` |
| `'l'`  | 2      | 1         | `1 // 2 = 0` ❌ (Not enough) |
| `'o'`  | 2      | 1         | `1 // 2 = 0` ❌ (Not enough) |
| `'n'`  | 1      | 1         | `1 // 1 = 1` |

❌ **Final Answer:** `min(1, 1, 0, 0, 1) = 0` → Cannot form "balloon".

---

## **Key Takeaways (Understanding vs. Memorization)**
1. **Recognize the problem type:**
   - This is a **letter frequency** problem, best solved with a **hash map (Counter)**.
   
2. **Understand the "bottleneck principle":**
   - The **letter that appears the fewest times** (after division) limits the maximum count of "balloon".
   
3. **Apply the same logic to other problems:**
   - If a word requires different letter frequencies, always find how many full words can be made based on the **least available letter**.

This **step-by-step thinking** helps you solve similar problems **without memorizing**. 🚀

---

## **Complexity Analysis**
- **Counting letters:** `O(N)` where `N` is the length of `text`
- **Checking constraints:** `O(1)` (only 5 letters in "balloon")
- **Overall Complexity:** `O(N)`, making it very efficient.

---

## **Similar Problems**
- **"Ransom Note" (LeetCode 383)** – Checking if we can form one word using letters from another.
- **"Find Words That Can Be Formed by Characters" (LeetCode 1160)** – Finding how many words can be formed given letter constraints.

If you understood this approach, you can now solve many problems **without memorizing**! 🚀🔥

