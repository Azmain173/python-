# Maximum Average Subarray I - LeetCode Problem

## Problem Statement
Given an array `nums` consisting of `n` integers, find a contiguous subarray of length `k` that has the **maximum average value**, and return this value. The answer should be a floating-point number with precision up to 5 decimal places.

### Constraints:
- `1 <= k <= n <= 10^5`
- `-10^4 <= nums[i] <= 10^4`

## Example
### **Input:**
```python
nums = [1,12,-5,-6,50,3]
k = 4
```
### **Output:**
```python
12.75000
```
### **Explanation:**
- The subarray `[12, -5, -6, 50]` has the maximum average `(12 + (-5) + (-6) + 50) / 4 = 12.75`.

---

## Approach
We can solve this problem efficiently using the **Sliding Window Technique**:
1. Compute the sum of the first `k` elements (initial window).
2. Slide the window across the array by removing the leftmost element and adding the next rightmost element.
3. Update the maximum average whenever a new window sum is computed.

This method ensures an **O(n)** time complexity, as we traverse the array only once.

---

## Corrected Python Solution
```python
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        
        # Compute the sum of the first k elements
        curr_sum = sum(nums[:k])
        max_average = curr_sum / k  # Initialize max_average with first k elements' average

        # Sliding window technique
        for i in range(k, n):
            curr_sum += nums[i] - nums[i - k]  # Add new element, remove old element
            max_average = max(max_average, curr_sum / k)

        return max_average
```

---

## Key Corrections in the Initial Approach
### **1️⃣ Incorrect First Loop Condition (`for i in range(0, k-1)`)**
- The loop should sum the first `k` elements, but `range(0, k-1)` iterates only `k-1` times, **missing the last element (`nums[k-1]`)**.
- Corrected using `sum(nums[:k])`.

### **2️⃣ Incorrect `max_average` Initialization**
- Originally initialized as `float('inf')`, which is incorrect since we need a **maximum**.
- Correct initialization: `max_average = curr_sum / k`.

### **3️⃣ Incorrect Second Loop Range (`for i in range(k, n-1)`)**
- `n-1` is incorrect because we need to slide the window until the last index.
- Correct range: `for i in range(k, n)`.

---

## Complexity Analysis
| **Aspect**  | **Complexity**  |
|------------|----------------|
| **Time Complexity** | O(n) (We traverse the array once) |
| **Space Complexity** | O(1) (We use only a few variables) |

---

## Edge Cases Considered
- `k = 1`: The function should return the maximum element from `nums`.
- Negative numbers: The function should correctly handle negative values in `nums`.
- Large input size: The function should handle `n = 100000` efficiently.

---

## Summary
- **Sliding Window Technique** optimizes the solution to **O(n)**.
- Fixed incorrect loop ranges and initialization errors.
- Ensured correct sum calculations and updates.

This solution efficiently finds the **maximum average subarray of size `k`**. 🚀
