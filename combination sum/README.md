# LeetCode 39: Combination Sum - Solution Explanation

## Problem Statement
Given an array of **distinct** integers `candidates` and a target integer `target`, return all unique combinations of `candidates` where the chosen numbers sum to `target`. The **same** number may be chosen from `candidates` **an unlimited number of times**.

### Example
#### Input:
```python
candidates = [2,3,6,7]
target = 7
```
#### Output:
```python
[[2,2,3],[7]]
```
#### Explanation:
- `2+2+3 = 7` ✅
- `7 = 7` ✅
- `3+3+?` ❌ (not possible to make 7)
- `6+?` ❌ (not possible to make 7)

---

## Code Breakdown

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
```
- This defines a class `Solution` with a method `combinationSum` that takes:
  - `candidates`: A list of distinct integers.
  - `target`: The target sum.
  - Returns a list of lists, where each inner list represents a valid combination summing to `target`.

```python
        res, sol = [], []
```
- `res`: Stores the final list of all valid combinations.
- `sol`: Temporarily stores the current combination being explored.

```python
        nums = candidates
        n = len(nums)
```
- `nums`: Simply an alias for `candidates`.
- `n`: The length of the candidates list.

```python
        def backtrack(i, curr_sum):
```
- Defines a **backtracking function** `backtrack(i, curr_sum)` where:
  - `i`: The current index in `candidates`.
  - `curr_sum`: The sum of elements currently in `sol`.

```python
            if curr_sum == target:
                res.append(sol[:])
                return
```
- If `curr_sum` matches `target`, a valid combination is found.
- Append a **copy** of `sol` to `res` and return.

```python
            if curr_sum > target or i == n:
                return
```
- If `curr_sum` exceeds `target` or we reach the end of `candidates`, stop further exploration.

```python
            backtrack(i+1, curr_sum)
```
- **Exclude** `nums[i]` and move to the next index.

```python
            sol.append(nums[i])
            backtrack(i, curr_sum + nums[i])  # Include `nums[i]` and continue at `i`
            sol.pop()
```
- **Include** `nums[i]` and call `backtrack(i, curr_sum + nums[i])`.
- Since we can **reuse** numbers, we call `backtrack(i, ...)` instead of `i+1`.
- Remove the last element from `sol` to backtrack and explore other possibilities.

```python
        backtrack(0, 0)
        return res
```
- Start backtracking from index `0` with `curr_sum = 0`.
- Return the final `res` containing all valid combinations.

---

## Example Walkthrough

Let's take `candidates = [2,3,6,7]` and `target = 7`.

### **Step-by-Step Execution:**
1. Start with `i = 0`, `curr_sum = 0`.
2. Try `2`:
   - `curr_sum = 2`, try another `2`:
     - `curr_sum = 4`, try another `2`:
       - `curr_sum = 6`, try another `2` (exceeds `7`, backtrack).
       - Try `3` (exceeds `7`, backtrack).
     - Remove `2`, try `3`:
       - `curr_sum = 7` ✅ (Add `[2,2,3]` to `res`).
3. Try `3` directly:
   - `curr_sum = 3`, try another `3`:
     - `curr_sum = 6`, try another `3` (exceeds `7`, backtrack).
   - Remove `3`, try `6`:
     - `curr_sum = 6`, try another `6` (exceeds `7`, backtrack).
   - Remove `6`, try `7`:
     - `curr_sum = 7` ✅ (Add `[7]` to `res`).

Final result: `[[2,2,3],[7]]` ✅

---

## **Time Complexity Analysis**
- Each number can be used multiple times, and we explore all possible combinations.
- The worst case occurs when `target` is large and we use the smallest number repeatedly.
- The complexity is **O(2^T)**, where `T` is the target value.
- Since we append and pop elements in `sol`, space complexity is **O(T)**.

---

## **Why This Works?**
1. **Backtracking** ensures we explore all valid combinations.
2. **Pruning** (`curr_sum > target` case) prevents unnecessary recursion.
3. **Choice to include or exclude** ensures we don't miss valid sums.
4. **Using `i` instead of `i+1`** allows repeated numbers in combinations.

This approach efficiently finds all valid combinations for any given target. 🚀
