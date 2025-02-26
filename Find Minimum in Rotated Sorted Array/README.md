# Find Minimum in Rotated Sorted Array

## Problem Statement
You are given a **rotated sorted array** (an ascending sorted array that has been rotated at some unknown pivot). Your task is to **find the minimum element** in O(log n) time.

**Example 1:**
```plaintext
Input: nums = [3,4,5,1,2]
Output: 1
```

**Example 2:**
```plaintext
Input: nums = [4,5,6,7,0,1,2]
Output: 0
```

**Example 3:**
```plaintext
Input: nums = [11,13,15,17]
Output: 11
```

## Approach
Since the array is rotated and sorted, we can use **Binary Search** to efficiently find the minimum element in O(log n) time.

### **Algorithm**
1. Initialize `left = 0` and `right = len(nums) - 1`.
2. Perform binary search while `left < right`:
   - Compute `mid = (left + right) // 2`.
   - If `nums[mid] > nums[right]`, the minimum is in the **right half** → `left = mid + 1`.
   - Otherwise, the minimum is in the **left half or mid itself** → `right = mid`.
3. When the loop exits, `left` will point to the minimum element.

## **Code Implementation**
```python
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
```

## **Why `while left < right` Instead of `while left <= right`?**
If we use `while left <= right`, it might cause an **extra iteration** when `left == right`, which is unnecessary.
Using `while left < right` ensures that we exit the loop at the correct moment and avoid redundant checks.

## **Time & Space Complexity**
- **Time Complexity:** O(log n) - Binary search reduces the search space by half in each iteration.
- **Space Complexity:** O(1) - We use only a few extra variables.

## **Edge Cases Considered**
- **Array not rotated:** `[1,2,3,4,5]` → Output: `1`
- **Single element:** `[3]` → Output: `3`
- **Already rotated at the smallest element:** `[2,3,4,5,1]` → Output: `1`
- **Fully sorted array:** `[1,2,3,4,5]` (which is a rotated version of itself) → Output: `1`

## **Conclusion**
This approach effectively finds the minimum element in O(log n) time using binary search, ensuring efficiency even for large inputs.

