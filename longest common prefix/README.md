Longest Common Prefix - LeetCode Problem
Problem Statement
Given an array of strings strs, find the longest common prefix among all the strings.

If there is no common prefix, return an empty string "".


Code Explanation
Initialize the Prefix:

Start with the first word as prefix.
This acts as the common prefix until we find a mismatch.
Iterate Through the List:

Compare prefix with each word in the list.
If the word doesn’t start with prefix, remove the last character (prefix = prefix[:-1]).
Repeat this until the word starts with the prefix or the prefix becomes empty.
Return the Final Prefix:

If at any point prefix becomes empty, return "".
Otherwise, return the common prefix found after checking all words.
Problems Faced & Solutions
1. Understanding prefix = prefix[:-1]
Initially, I wasn’t sure how removing the last character helped.
After debugging, I realized it shrinks the prefix step-by-step until it matches all words.
2. Handling Edge Cases
When an empty string is in the list, the prefix should immediately return "".
If all words are the same, the prefix should return the full word.
3. Performance Concerns
Instead of comparing characters one by one, using startswith() and reducing prefix makes it more efficient.
