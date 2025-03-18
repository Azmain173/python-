# README: LeetCode 17 - Letter Combinations of a Phone Number

## Problem Statement
Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. The mapping of digits to letters follows the telephone keypad:

```
2 -> "abc"
3 -> "def"
4 -> "ghi"
5 -> "jkl"
6 -> "mno"
7 -> "pqrs"
8 -> "tuv"
9 -> "wxyz"
```

## Solution Explanation

### Code:
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []

        res, sol = [], []  # res stores final results, sol is a temporary list for building combinations
        n = len(digits)  # Length of input digits string
        
        # Mapping of digits to letters based on a phone keypad
        dict1 = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(i):
            if i == n:  # If we reach the length of digits, we have formed a combination
                res.append("".join(sol))  # Join list into string and add to result
                return
            
            # Iterate through possible letters for the current digit
            for letter in dict1[digits[i]]:
                sol.append(letter)  # Choose a letter
                backtrack(i + 1)  # Move to the next digit
                sol.pop()  # Undo choice (backtrack)
        
        backtrack(0)  # Start recursion from the first digit
        return res  # Return the list of all letter combinations
```

### Step-by-Step Execution with Example
#### Example Input:
```python
Input: digits = "23"
```
#### Execution Flow:
1. **Initial check:** Since `digits` is not empty, we proceed.
2. **Backtracking starts at index `0` (digit '2'):**
   - Options: "a", "b", "c"
   - Pick "a", move to next index.
3. **Backtracking at index `1` (digit '3'):**
   - Options: "d", "e", "f"
   - Pick "d", form "ad", add to `res`.
   - Undo "d", pick "e", form "ae", add to `res`.
   - Undo "e", pick "f", form "af", add to `res`.
4. **Backtrack to index `0`, pick next letter ('b') and repeat step 3.**
5. **Continue until all combinations are generated.**

#### Example Output:
```python
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

## Complexity Analysis
- **Time Complexity:** O(3^n × 4^m), where `n` is the count of digits mapped to 3 letters (2,3,4,5,6,8) and `m` is the count of digits mapped to 4 letters (7,9). This represents the number of recursive calls.
- **Space Complexity:** O(n), where `n` is the length of `digits` (depth of the recursion stack).

## Summary
This solution efficiently generates all possible letter combinations using **backtracking**. It systematically explores all options while maintaining correctness using recursion and backtracking principles.

