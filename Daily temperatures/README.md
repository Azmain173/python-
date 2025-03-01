# README: Understanding the `dailyTemperatures` Function

## Problem Statement:
The `dailyTemperatures` function takes a list of temperatures as input and returns a list where each element represents the number of days until a warmer temperature appears. If there is no future day with a warmer temperature, the value remains `0`.

## Code Breakdown:

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
```
- Defines a class `Solution` containing the function `dailyTemperatures`.
- The function takes `temperatures` (a list of integers) as input and returns a list of integers.

```python
        temp = temperatures
```
- Creates a new reference `temp` to the input list `temperatures`.
- This is unnecessary as `temperatures` can be used directly.

```python
        n = len(temp)
```
- Stores the length of the temperature list in `n` for easier access.

```python
        answer = [0] * n
```
- Initializes a list `answer` of size `n`, filled with zeros.
- Each element in `answer` will store the number of days until a warmer temperature appears.

```python
        stack = []
```
- Initializes an empty stack to keep track of temperatures and their indices.
- The stack will help efficiently find the next warmer temperature using a **monotonic decreasing stack** approach.

```python
        for i, t in enumerate(temp):
```
- Iterates through the list of temperatures.
- `enumerate(temp)` generates both the index (`i`) and temperature value (`t`).
- **Problem:** Initially, you wrote `for t, i`, which is incorrect because `enumerate()` provides `(index, value)`, so `i` should come first.

```python
            while stack and stack[-1][0] < t:
```
- Runs a loop while the stack is not empty and the top element of the stack (which holds a temperature) is smaller than the current temperature `t`.
- **Key observation:** We store **tuples** `(temperature, index)` in the stack but only compare the first value (`t`), which is correct because we only need the temperature for comparison.

```python
                stack_t, stack_i = stack.pop()
```
- Removes the top element from the stack.
- `stack_t` stores the temperature, and `stack_i` stores the index.

```python
                answer[stack_i] = i - stack_i
```
- Calculates the number of days until a warmer temperature appears.
- The difference `i - stack_i` gives the number of days between the stored temperature and the current one.

```python
            stack.append((t, i))
```
- Pushes the current temperature and its index as a tuple `(t, i)` onto the stack.
- This ensures the stack maintains temperatures in a decreasing order (new temperatures are pushed only if they are smaller than the top).

```python
        return answer
```
- Returns the computed `answer` list, which contains the number of days until a warmer temperature appears for each index.

## Issues Noticed and Fixes:
1. **Incorrect tuple unpacking order in the loop:**
   - You initially wrote `for t, i in enumerate(temp)`, but `enumerate()` returns `(index, value)`, so it should be `for i, t`.
2. **Tuple structure usage in stack:**
   - You store `(temperature, index)` tuples in the stack but only compare `temperature` in `while stack and stack[-1][0] < t:`.
   - This is correct behavior because we only need the temperature for comparison.

## Explanation of Stack Usage:
- The stack maintains temperatures in a **monotonic decreasing order**.
- If a temperature `t` is higher than the top element in the stack, we pop elements until we find a warmer day.
- This ensures efficient **O(n) complexity** because each element is pushed and popped at most once.

## Example Walkthrough:
### Input:
```python
[73, 74, 75, 71, 69, 72, 76, 73]
```
### Step-by-Step Execution:
| Index | Temperature | Stack (Before)   | Action                       | Stack (After)  | Answer         |
|--------|-------------|------------------|-----------------------------|-----------------|---------------|
| 0      | 73          | []               | Push (73,0)                 | [(73,0)]        | [0,0,0,0,0,0,0,0] |
| 1      | 74          | [(73,0)]         | Pop (73,0), Push (74,1)     | [(74,1)]        | [1,0,0,0,0,0,0,0] |
| 2      | 75          | [(74,1)]         | Pop (74,1), Push (75,2)     | [(75,2)]        | [1,1,0,0,0,0,0,0] |
| 3      | 71          | [(75,2)]         | Push (71,3)                 | [(75,2), (71,3)] | [1,1,0,0,0,0,0,0] |
| 4      | 69          | [(75,2), (71,3)] | Push (69,4)                 | [(75,2), (71,3), (69,4)] | [1,1,0,0,0,0,0,0] |
| 5      | 72          | [(75,2), (71,3), (69,4)] | Pop (69,4), Pop (71,3), Push (72,5) | [(75,2), (72,5)] | [1,1,0,2,1,0,0,0] |
| 6      | 76          | [(75,2), (72,5)] | Pop (72,5), Pop (75,2), Push (76,6) | [(76,6)] | [1,1,4,2,1,1,0,0] |
| 7      | 73          | [(76,6)]         | Push (73,7)                 | [(76,6), (73,7)] | [1,1,4,2,1,1,0,0] |

### Final Output:
```python
[1, 1, 4, 2, 1, 1, 0, 0]
```

## Complexity Analysis:
- **Time Complexity:** O(n) → Each temperature is pushed and popped at most once.
- **Space Complexity:** O(n) → Stack stores at most `n` elements in the worst case.

## Conclusion:
- The function efficiently calculates the days required for the next warmer temperature using a **monotonic decreasing stack**.
- **Key mistakes you fixed:**
  - Using `for i, t` instead of `for t, i`.
  - Understanding how tuple `(t, i)` works: **comparison uses only `t`, but full tuple is stored in the stack**.

This README should give you a complete understanding of how your code works and the fixes you made!

