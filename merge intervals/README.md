
# Merge Intervals - Problem Solution

## Problem Description
Given a collection of intervals, merge all overlapping intervals.

### Input:
- A list of intervals, where each interval is represented as a pair `[start, end]` indicating a range from start to end.
- Intervals may overlap, and we are tasked with merging the intervals such that no two intervals overlap.

### Output:
- A list of non-overlapping intervals that covers all the intervals in the input.

### Example:

#### Input:
```python
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
```

#### Output:
```python
[[1, 6], [8, 10], [15, 18]]
```

---

## Approach

### Step-by-Step Explanation:

1. **Sort the Intervals:**
   - We begin by sorting the intervals based on the **start time** of each interval. Sorting helps us easily check if two intervals overlap.
   - Sorting is done using the `sort()` method and sorting by the first element (`start` time) of each interval.

2. **Iterate Through Sorted Intervals:**
   - We loop through the sorted intervals and check whether the current interval overlaps with the previous one:
     - If **no overlap** exists, we append the current interval to the result list (`merge`).
     - If **overlap** exists, we merge the intervals by updating the end time of the last merged interval to be the maximum of the current and previous intervals.

3. **Return the Result:**
   - Once all intervals are processed, the `merge` list contains the non-overlapping intervals.

---

## Time Complexity

### Time Complexity Analysis:

1. **Sorting:**
   - Sorting the list of intervals takes **O(n log n)** time, where **n** is the number of intervals.

2. **Iterating Through Intervals:**
   - After sorting, we loop through the intervals once to check for overlaps and merge intervals. This step takes **O(n)** time.

### Final Time Complexity:
- **O(n log n)** due to sorting.

### Space Complexity:
- **O(n)** as we are storing the merged intervals in a new list.

---

## Python Code Implementation:

```python
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Initialize the result list to store merged intervals
        merge = []

        # Sort intervals based on the starting point of each interval
        intervals.sort(key=lambda interval: interval[0])

        # Iterate through each interval in the sorted list
        for interval in intervals:
            # If there is no overlap or merge list is empty, add the interval
            if not merge or merge[-1][1] < interval[0]:
                merge.append(interval)
            else:
                # There is an overlap, so merge the intervals
                merge[-1] = [merge[-1][0], max(merge[-1][1], interval[1])]
        
        return merge
```

---

## Line-by-Line Explanation of Code:

1. `from typing import List`
   - **Imports the `List` type from Python's `typing` module** to specify that the input and output parameters of the `merge` method are lists of lists of integers.

2. `class Solution:`
   - **Defines the `Solution` class**, where we will implement our method for solving the merge intervals problem.

3. `def merge(self, intervals: List[List[int]]) -> List[List[int]]:`
   - **Defines the `merge` method** inside the `Solution` class. This method takes as input a list of intervals (`List[List[int]]`) and returns a list of merged intervals (`List[List[int]]`).

4. `merge = []`
   - **Initializes an empty list `merge`**, which will hold the final list of merged intervals.

5. `intervals.sort(key=lambda interval: interval[0])`
   - **Sorts the intervals** based on the starting time of each interval. The sorting is done using a **lambda function**, which returns the first element (`interval[0]`) of each interval. This ensures that intervals are sorted in increasing order of their start time.

6. `for interval in intervals:`
   - **Starts a loop to iterate through each interval** in the sorted list of intervals.

7. `if not merge or merge[-1][1] < interval[0]:`
   - **Checks if the `merge` list is empty or if there is no overlap** between the current interval and the last interval in the `merge` list.
     - If the `merge` list is empty (i.e., no intervals have been merged yet) or if the end time of the last merged interval (`merge[-1][1]`) is less than the start time of the current interval (`interval[0]`), it means there is no overlap.
     - In this case, **the current interval is added to the `merge` list**.

8. `merge.append(interval)`
   - **Appends the current interval to the `merge` list** if there is no overlap with the last interval.

9. `else:`
   - **Handles the case when an overlap exists** between the current interval and the last interval in `merge`.

10. `merge[-1] = [merge[-1][0], max(merge[-1][1], interval[1])]`
    - **Merges the current interval with the last merged interval**:
      - The start time of the merged interval is the same as the start time of the last merged interval (`merge[-1][0]`).
      - The end time of the merged interval is the maximum of the end times of the last merged interval (`merge[-1][1]`) and the current interval (`interval[1]`), ensuring the merged interval covers both intervals.

11. `return merge`
    - **Returns the final list of merged intervals** after processing all intervals.

---

## Questions and Answers:

### 1. **Why does sorting the intervals matter?**
   - Sorting ensures that we can easily compare consecutive intervals to check if they overlap. Without sorting, we would need to compare each interval with every other interval, leading to a more complex solution.

### 2. **What is the time complexity of this solution?**
   - **O(n log n)**: The sorting step is the most expensive part of the solution, where `n` is the number of intervals.

### 3. **What happens when there is no overlap?**
   - If the current interval does not overlap with the last interval in the `merge` list, we simply append it to `merge`.

### 4. **How do we merge intervals?**
   - When we detect an overlap, we modify the last interval in `merge` by updating its end time to the maximum of the current interval's end time and the last merged interval's end time.

---

## Conclusion:

This solution efficiently merges intervals with a time complexity of **O(n log n)**, which is the result of sorting. The space complexity is **O(n)** due to the storage of the result list.
