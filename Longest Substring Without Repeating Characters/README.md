# Longest Substring Without Repeating Characters - Code Explanation

## Problem Statement
Given a string `s`, find the length of the longest substring that does not contain repeating characters.

## Approach
The problem is solved using the **Sliding Window** technique. We maintain a window `[left, right]` where all characters are unique. If we encounter a duplicate, we adjust the window by moving `left` until the duplicate is removed.

## Code
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0  # Stores the maximum length of substring found
        sett = set()  # Stores unique characters within the current window
        n = len(s)    # Length of the input string
        left = 0      # Left boundary of the sliding window

        for right in range(n):  # Right pointer expands the window
            while s[right] in sett:  # If duplicate found, shrink window
                sett.remove(s[left])  # Remove leftmost character
                left += 1  # Move left pointer forward
            
            w = (right - left) + 1  # Calculate current window size
            longest = max(longest, w)  # Update the maximum length
            sett.add(s[right])  # Add the new character to the set
        
        return longest  # Return the maximum length found
```

## Explanation (Line by Line)

### **Class and Function Definition**
```python
class Solution:
```
- Defines a class `Solution` following LeetCode's format.

```python
    def lengthOfLongestSubstring(self, s: str) -> int:
```
- Defines a method `lengthOfLongestSubstring` that takes a string `s` as input and returns an integer (the length of the longest unique substring).

### **Variable Initialization**
```python
        longest = 0  
```
- `longest` keeps track of the maximum length of a substring without repeating characters.

```python
        sett = set()
```
- A `set` is used to store unique characters within the current window.

```python
        n = len(s)
```
- `n` holds the length of the input string.

```python
        left = 0
```
- `left` represents the starting index of the current window.

### **Expanding the Sliding Window**
```python
        for right in range(n):
```
- `right` iterates through the string, expanding the window to the right.

### **Handling Duplicate Characters**
```python
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
```
- If `s[right]` is already in the `set`, it means we found a duplicate.
- The loop removes characters from the left side (`s[left]`) until the duplicate is removed.
- `left` moves forward to shrink the window and maintain uniqueness.

### **Updating the Maximum Length**
```python
            w = (right - left) + 1
            longest = max(longest, w)
```
- `w = (right - left) + 1` computes the current window size.
- `longest` stores the maximum substring length found so far.

### **Adding New Character to Set**
```python
            sett.add(s[right])
```
- Adds `s[right]` to the `set` since it is now part of the valid window.

### **Returning the Result**
```python
        return longest
```
- Returns the length of the longest substring without repeating characters.

## **Time and Space Complexity**
### **Time Complexity: O(n)**
- Each character is processed at most twice (once when added and once when removed), leading to a linear time complexity.

### **Space Complexity: O(min(n, 26))**
- The space complexity is determined by the `set`, which stores unique characters.
- Since there are at most 26 lowercase English letters, the maximum space used is `O(26) = O(1)`. However, for arbitrary strings, it could be `O(n)`.

## **Example Walkthrough**
### **Example 1**
#### Input:
```python
s = "abcabcbb"
```
#### Steps:
1. `right=0`, add 'a' → `sett = {a}`, longest = 1
2. `right=1`, add 'b' → `sett = {a, b}`, longest = 2
3. `right=2`, add 'c' → `sett = {a, b, c}`, longest = 3
4. `right=3`, 'a' repeats → remove 'a' and shift `left`
5. Continue processing, updating `longest` accordingly.

#### Output:
```python
3
```

### **Example 2**
#### Input:
```python
s = "bbbbb"
```
#### Output:
```python
1
```

### **Example 3**
#### Input:
```python
s = "pwwkew"
```
#### Output:
```python
3
```

## Summary
- **Sliding Window Technique** efficiently finds substrings.
- **Set Data Structure** ensures uniqueness.
- **O(n) Time Complexity** ensures scalability for large inputs.

This method provides an optimal solution for finding the longest substring without repeating characters.

