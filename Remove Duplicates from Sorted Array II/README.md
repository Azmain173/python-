# LeetCode 80 - Remove Duplicates from Sorted Array II

This README explains the line-by-line logic behind the following solution for LeetCode problem 80:

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        count = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j
```

## Problem Summary
You're given a **sorted array**, and you need to remove duplicates **in-place** such that **each element appears at most twice**. The function should return the **new length** of the modified array.

---

## Example Input
```python
nums = [1, 1, 1, 2, 2, 3]
```

### Expected Output
```python
[1, 1, 2, 2, 3]
# New length = 5
```

---

## Line-by-Line Explanation

### Line 1: Class Definition
```python
class Solution:
```
Defines a class named `Solution` which contains our solution method.

### Line 2: Method Declaration
```python
def removeDuplicates(self, nums: List[int]) -> int:
```
Defines a method `removeDuplicates` that takes a list of integers (`nums`) and returns an integer (the new length).

### Line 3: Initialize j = 1
```python
j = 1
```
`j` is a pointer to the position in the array where the next allowed value should go. Starts at 1 because the first element is always allowed.

### Line 4: Initialize count = 1
```python
count = 1
```
Keeps track of how many times the current number has appeared.

### Line 5: Get the length of the array
```python
n = len(nums)
```
Stores the length of the array for easier reference.

### Line 6: Loop through the array from index 1
```python
for i in range(1, n):
```
Starts at index 1 and iterates through the array.

### Line 7-9: Update count based on duplicates
```python
if nums[i] == nums[i - 1]:
    count += 1
else:
    count = 1
```
- If current element is the same as the previous one, increment count.
- Otherwise, reset count to 1 (new number).

### Line 10-12: If valid (≤2 occurrences), copy to nums[j]
```python
if count <= 2:
    nums[j] = nums[i]
    j += 1
```
- If the count is ≤ 2, the number is allowed.
- Write it at index `j`.
- Increment `j` for the next possible valid number.

### Line 13: Return the new length
```python
return j
```
Returns the new length of the array — which is how many valid numbers we have kept.

---

## Walkthrough with Example
```python
nums = [1, 1, 1, 2, 2, 3]
```
Step-by-step:

| i | nums[i] | count | nums (in-place)       | j (new length) |
|---|---------|--------|------------------------|-----------------|
| 1 |   1     |   2    | [1, 1, 1, 2, 2, 3]     | 2               |
| 2 |   1     |   3    | [1, 1, 1, 2, 2, 3]     | 2 (no change)   |
| 3 |   2     |   1    | [1, 1, 2, 2, 2, 3]     | 3               |
| 4 |   2     |   2    | [1, 1, 2, 2, 2, 3]     | 4               |
| 5 |   3     |   1    | [1, 1, 2, 2, 3, 3]     | 5               |

Final array (first 5 elements): `[1, 1, 2, 2, 3]`

---

## Summary
- Use `j` as a write pointer.
- Use `count` to track occurrences.
- Copy valid elements to `nums[j]`, and increase `j` accordingly.
- Return `j` as the new length.

This approach ensures **O(n)** time and **O(1)** extra space.

