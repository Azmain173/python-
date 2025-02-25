# Valid Palindrome - LeetCode Problem

## Problem Statement
Given a string `s`, determine if it is a **palindrome**, considering only **alphanumeric characters** and **ignoring cases**.

### **Example 1:**
#### **Input:**
```python
s = "A man, a plan, a canal: Panama"
```
#### **Output:**
```python
True
```
#### **Explanation:**
Ignoring spaces and punctuation, the string becomes `"amanaplanacanalpanama"`, which is a palindrome.

---
### **Example 2:**
#### **Input:**
```python
s = "race a car"
```
#### **Output:**
```python
False
```
#### **Explanation:**
After removing non-alphanumeric characters and converting to lowercase, the string becomes `"raceacar"`, which is **not** a palindrome.

---
### **Example 3:**
#### **Input:**
```python
s = " "
```
#### **Output:**
```python
True
```
#### **Explanation:**
An empty string or a string with only spaces is considered a palindrome.

---
## **Approach 1: Using Filtering and Two Pointers** (Preferred Approach)
### **Steps:**
1. Convert the string to lowercase.
2. Filter out only alphanumeric characters.
3. Use a **two-pointer technique** to compare characters from both ends.

### **Code:**
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase
        s = s.lower()
        
        # Keep only alphanumeric characters
        filtered_str = "".join([ch for ch in s if ch.isalnum()])
        
        # Two-pointer approach
        left, right = 0, len(filtered_str) - 1
        
        while left < right:
            if filtered_str[left] != filtered_str[right]:
                return False
            left += 1
            right -= 1
        
        return True
```

### **Time Complexity:** `O(n)`  
### **Space Complexity:** `O(n)` (because of `filtered_str`)

---
## **Alternative Approach: Two Pointers Without Extra Space**
Instead of creating a new filtered string, we can check characters **in-place** while iterating.

### **Code:**
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # Move left pointer if not alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            # Move right pointer if not alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1
            
            # Compare characters (ignoring case)
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True
```

### **Time Complexity:** `O(n)`  
### **Space Complexity:** `O(1)` (No extra string storage)

---
## **Key Takeaways**
- **Filtering Method:** Uses `.join()` with list comprehension to remove non-alphanumeric characters.
- **Two-Pointer Technique:** Moves `left` and `right` towards the center while comparing characters.
- **Lowercasing:** Ensures case-insensitive comparison.
- **Alternative Approach:** Uses in-place character checking without extra space.

---
## **Conclusion**
The problem can be solved using **two main approaches:**
1. **Filtering first and then using two pointers** *(Easy to understand but uses extra space)*
2. **Checking characters in-place with two pointers** *(Optimized for space but slightly harder to follow)*

Both approaches work in `O(n)` time, but the second one saves space. However, for readability and simplicity, the **first approach** (with `filtered_str`) is preferred.

---
**Hope this helps! Happy Coding! 🚀**

