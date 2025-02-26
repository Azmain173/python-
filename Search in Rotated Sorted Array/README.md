# Search in Rotated Sorted Array

## Problem Statement
You are given a **rotated sorted array** and a **target value**. Your task is to find the index of the target in **O(log n)** time. If the target does not exist, return `-1`.

### Example 1:
```plaintext
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

### Example 2:
```plaintext
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

## Approach
This problem is an extension of **Find Minimum in Rotated Sorted Array**. We first **find the index of the minimum element**, which is the rotation point, and then apply **binary search** in the appropriate subarray.

### **Steps to Solve the Problem**
1. **Find the minimum element (rotation point) using binary search**:  
   - This part is the same as the previous problem.
   - We determine if the **middle element is greater than the rightmost element** to decide which half to search in.
   - When we find the minimum element, its index (`min_index`) helps split the array into two sorted subarrays.

2. **Decide which subarray to perform binary search on**:  
   - If `min_index == 0`, the array is not rotated, so search the entire array.
   - If `target` lies in the left sorted half (`nums[0]` to `nums[min_index-1]`), search in that range.
   - Otherwise, search in the right sorted half (`nums[min_index]` to `nums[n-1]`).

3. **Perform standard binary search** on the chosen subarray.

---

## **Code Implementation**
```python
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        # Step 1: Find the rotation index (minimum element)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        min_index = left

        # Step 2: Decide the search range based on target
        if min_index == 0:
            left, right = 0, n - 1
        elif nums[0] <= target <= nums[min_index - 1]:
            left, right = 0, min_index - 1
        else:
            left, right = min_index, n - 1
        
        # Step 3: Perform binary search in the selected subarray
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1
```

---

## **How This Builds on the Previous Problem**
1. **Finding the Rotation Point**: We reuse the logic from **Find Minimum in Rotated Sorted Array** to efficiently find the smallest element's index (`min_index`).
2. **Dividing the Search Space**: Based on `min_index`, we identify which part of the array is sorted and where the target might be.
3. **Binary Search**: We apply regular binary search to find the target efficiently.

---

## **Time & Space Complexity**
- **Time Complexity:** O(log n) - Finding the rotation point takes O(log n), and binary search takes O(log n), so the total is O(log n).
- **Space Complexity:** O(1) - We use only a few extra variables.

---

## **Edge Cases Considered**
- **Target is the minimum element:** `[3,4,5,1,2]`, target = `1`
- **Array not rotated:** `[1,2,3,4,5]`, target = `3`
- **Target not in the array:** `[4,5,6,7,0,1,2]`, target = `10`
- **Single element array:** `[3]`, target = `3`

---

## **Conclusion**
By leveraging the **Find Minimum in Rotated Sorted Array** problem, we efficiently solve the search problem in O(log n) time using **binary search** twice.
