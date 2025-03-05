# Longest Repeating Character Replacement - Code Explanation

## Problem Statement
The problem requires us to find the length of the longest substring that contains the same letter after performing at most `k` replacements.

## Code Breakdown
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest=0
        left=0
        n=len(s)
        counts=[0]*26
        for right in range(n):
            counts[ord(s[right])-65]+=1
            while (right-left+1)-max(counts)>k:
                counts[ord(s[left])-65]-=1
                left+=1
            longest=max(longest,(right-left+1))
        return longest
```

### Explanation

#### **Class and Method Definition**
```python
class Solution:
```
- Defines a class named `Solution` which follows LeetCode's format for defining solutions.

```python
    def characterReplacement(self, s: str, k: int) -> int:
```
- Defines a method `characterReplacement` within the `Solution` class.
- `s: str` -> The input string.
- `k: int` -> The number of allowed character replacements.
- `-> int` -> The function returns an integer representing the length of the longest valid substring.

#### **Variable Initialization**
```python
        longest=0
```
- Initializes `longest` to store the maximum length of the substring found.

```python
        left=0
```
- `left` represents the left pointer of the sliding window.

```python
        n=len(s)
```
- `n` stores the length of the input string `s`.

```python
        counts=[0]*26
```
- `counts` is a list of size 26 (representing the 26 uppercase English letters).
- It stores the frequency of each character within the current window.

#### **Sliding Window Expansion**
```python
        for right in range(n):
```
- Iterates through the string with the `right` pointer expanding the window.

```python
            counts[ord(s[right])-65]+=1
```
- `ord(s[right])` gives the ASCII value of the character.
- `ord('A')` is 65, so subtracting 65 maps 'A' to index 0, 'B' to index 1, ..., 'Z' to index 25.
- Increments the count of the current character in the `counts` array.

#### **Sliding Window Contraction**
```python
            while (right-left+1)-max(counts)>k:
```
- `(right - left + 1)` is the length of the current window.
- `max(counts)` gives the count of the most frequently occurring character in the window.
- `(right - left + 1) - max(counts)` calculates how many characters need to be replaced to make all characters in the window the same.
- If this value exceeds `k`, the window is too large and must be shrunk.

```python
                counts[ord(s[left])-65]-=1
```
- Decreases the count of `s[left]` as the left pointer moves.

```python
                left+=1
```
- Moves the left pointer forward to shrink the window.

#### **Updating the Maximum Length**
```python
            longest=max(longest,(right-left+1))
```
- Updates `longest` with the maximum length of a valid window found so far.

#### **Return the Result**
```python
        return longest
```
- Returns the length of the longest substring that meets the condition.

## Summary
- Uses the **Sliding Window** technique.
- Maintains a frequency array `counts` for quick access to character counts.
- Expands the window using `right`, shrinks it using `left` when necessary.
- The core condition `(right - left + 1) - max(counts) > k` ensures at most `k` replacements.
- Efficient **O(n)** time complexity due to linear iteration.

This approach ensures an optimal and efficient solution to the problem!

