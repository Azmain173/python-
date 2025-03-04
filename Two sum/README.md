# Two Sum Problem - LeetCode Solution

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers that add up to `target`.

You **may not use the same element twice**, and you can assume that **exactly one solution exists**.

### Example 1:
```python
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

## Solution Using HashMap (Dictionary in Python)
To solve this problem efficiently, we use a **hashmap (dictionary)** to store the numbers we have seen so far and their indices. This allows us to find the complement (the number required to reach the target) in constant time `O(1)`.

### **Algorithm**
1. Create an empty **hashmap** to store numbers and their indices.
2. Iterate through the array:
   - Calculate the **complement** as `target - num`.
   - If the complement exists in the hashmap, return its index along with the current index.
   - Otherwise, store the current number and its index in the hashmap.

### **Code Implementation (Python)**
```python
def twoSum(nums, target):
    num_map = {}  # Dictionary to store numbers and their indices
    for i, num in enumerate(nums):
        complement = target - num  # The number we need to find
        if complement in num_map:  # Check if complement is already stored
            return [num_map[complement], i]  # Found solution
        num_map[num] = i  # Store current number's index
    return []  # Return empty if no solution is found
```

### **Step-by-Step Execution**
#### **Example:**
```python
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]
```

#### **Iteration Details:**
| Index (i) | Num | Complement (target - num) | HashMap State | Condition Check |
|-----------|-----|--------------------------|---------------|----------------|
| 0         | 2   | 9 - 2 = 7                | `{2: 0}`      | 7 not in hashmap |
| 1         | 7   | 9 - 7 = 2                | `{2: 0}`      | **2 found in hashmap → return [0,1]** |

### **Understanding `complement = target - num`**
- `i` represents the **index** of the number in the array.
- `num` represents the **value** at that index.
- `complement = target - num` is the number we need to reach `target`.
- We check if this complement is **already in the hashmap**.

### **Why return `[num_map[complement], i]`?**
- `num_map[complement]` gives the **index of the previously seen number**.
- `i` is the **index of the current number**.
- Together, these indices form the correct answer.

## **Time Complexity Analysis**
- **Using a brute-force approach** (nested loops) would take `O(n^2)`, which is inefficient.
- **Using a hashmap**, we achieve an **O(n) time complexity**, as we only traverse the list once.
- **Space complexity is O(n)**, as we store numbers in the hashmap.

## **Final Thoughts**
Using a hashmap is an optimal way to solve the **Two Sum** problem, as it allows checking for complements in **constant time O(1)**. The overall approach ensures a **single pass (O(n) time complexity)**, making it much faster than brute force methods.

