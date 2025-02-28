# Understanding the Group Anagrams Solution in Python

## **Introduction**
The problem of grouping anagrams involves taking a list of words and categorizing them based on whether they are anagrams of each other. An anagram is a word formed by rearranging the letters of another word. For example, "bat" and "tab" are anagrams, as they contain the same letters in different orders.

This document explains the logic behind an efficient Python solution to the problem using a **dictionary with tuple keys** representing character frequencies. It also includes frequently asked questions and detailed examples.

---

## **Frequently Asked Questions (FAQs)**

### **Q: What is the main logic in this code?**
The main logic lies in computing a **unique key** for each word based on the count of its letters. If two words have the same key (i.e., the same letter frequency tuple), they are anagrams and are grouped together.

### **Q: How does the key work as a tuple?**
The tuple represents the frequency of each letter in the word. Since a tuple is immutable and hashable, it can be used as a dictionary key. If two words generate the same tuple, they are stored in the same list.

### **Q: How does the program check whether two words are anagrams?**
The words are **not compared directly**. Instead, their letter frequency tuple is compared. If two words have the same tuple, they are considered anagrams.

### **Q: Why is a tuple used instead of a list for the key?**
A list is mutable and cannot be used as a dictionary key, whereas a tuple is immutable and hashable, making it suitable for dictionary lookup.

### **Q: How does the dictionary store and retrieve anagrams?**
Each unique tuple key points to a list. Words with the same tuple are appended to the same list.

---

## **Step-by-Step Breakdown of the Code**

### **1. Importing Required Module**
```python
from collections import defaultdict
```
- `defaultdict` is a special dictionary from the `collections` module that automatically initializes values for missing keys.
- Here, it is used to store lists of anagram words under the same key.

### **2. Defining the Function**
```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
```
- `class Solution:` defines a class, which is a common format for LeetCode problems.
- `groupAnagrams(self, strs: List[str])` is a method that takes `strs` (a list of strings) as input and returns a list of lists containing grouped anagrams.

### **3. Initializing the Dictionary**
```python
anagrams_dict = defaultdict(list)
```
- `anagrams_dict` is a dictionary where:
  - **Keys** are tuples representing letter frequency counts.
  - **Values** are lists of words that match that frequency pattern (i.e., anagrams).
- The `defaultdict(list)` ensures that missing keys automatically get an empty list.

### **4. Processing Each Word in `strs`**
```python
for s in strs:
```
- This loop iterates over each word `s` in the input list `strs`.

### **5. Creating a Character Frequency Count**
```python
count = [0] * 26
```
- A list of 26 zeroes is created to represent the counts of letters 'a' to 'z'.
- The index positions correspond to letters: 0 → 'a', 1 → 'b', ..., 25 → 'z'.

### **6. Updating the Letter Frequency List**
```python
for c in s:
    count[ord(c) - ord('a')] += 1
```
- Each letter in `s` updates the `count` list.
- `ord(c) - ord('a')` gives the index for the letter:
  - `'a'` → `0`
  - `'b'` → `1`
  - `'c'` → `2`, etc.
- This ensures that the frequency list correctly represents the number of times each letter appears in `s`.

### **7. Converting the List to a Tuple (Key for Dictionary)**
```python
key = tuple(count)
```
- The list `count` is **converted into a tuple** to be used as a dictionary key.
- Tuples are immutable and hashable, making them valid dictionary keys.

### **8. Storing Words Under the Same Key**
```python
anagrams_dict[key].append(s)
```
- If another word has the same **tuple key**, it will be stored in the same list.
- Example:

#### **Example Table of Key Generation**
| Word  | Letter Frequency Key (Tuple) | Grouped Anagrams |
|--------|-------------------------|-----------------|
| "bat"  | (1, 1, 0, ..., 1) | ["bat", "tab"] |
| "tab"  | (1, 1, 0, ..., 1) | ["bat", "tab"] |
| "cat"  | (1, 0, 1, ..., 1) | ["cat", "act", "tac"] |
| "act"  | (1, 0, 1, ..., 1) | ["cat", "act", "tac"] |
| "tac"  | (1, 0, 1, ..., 1) | ["cat", "act", "tac"] |

### **9. Returning the Grouped Anagrams**
```python
return anagrams_dict.values()
```
- `anagrams_dict.values()` extracts all grouped lists of anagrams and returns them.
- Output Example:
  ```python
  [["bat", "tab"], ["cat", "act", "tac"]]
  ```

---

## **How the Comparison Works**
- **We do not directly compare words character by character.**
- Instead, we compare their **tuple keys** (which are derived from letter frequencies).
- If two words have the same **tuple key**, they are **anagrams** and are stored in the same list.

Example:
```python
if key1 == key2:
    # They are anagrams and will be stored together.
```
- Instead of sorting each word (which takes O(N log N)), we just compare a tuple (O(1)).

---

## **Why is This Solution Efficient?**
1. **Avoids Sorting Each Word**
   - Sorting each word would take **O(N log N)**, but counting letters is **O(1)** (since the count list is always size 26).
2. **Efficient Dictionary Lookup**
   - Checking for existing keys and inserting values in a dictionary is **O(1)**.
3. **Overall Complexity:** **O(N * M)**
   - `N` = number of words.
   - `M` = average length of a word (fixed at 26 for English lowercase letters).
   - **Much faster than O(N * M log M) (sorting-based approach).**

---

## **Final Summary**
1. **Convert each word into a tuple-based frequency key.**
2. **Store anagrams under the same key in a dictionary.**
3. **Extract grouped anagram lists from the dictionary.**
4. **Tuple-based comparison ensures efficiency.**

This approach provides an **optimal** and **clean** solution to the problem of grouping anagrams. 🚀

