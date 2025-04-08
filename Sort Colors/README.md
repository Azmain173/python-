**LinkedIn Article: Mastering LeetCode 75 - Dutch National Flag Algorithm in Action**

If you're preparing for coding interviews, you've likely come across LeetCode Problem 75: **Sort Colors**. It's not just another sorting problem; it's a brilliant test of your understanding of **in-place sorting**, **two pointers**, and the classic **Dutch National Flag algorithm**.

### 🔗 The Problem
You're given an array `nums` containing only `0`, `1`, and `2`, representing red, white, and blue. Your task is to sort the array in-place so that all `0`s come first, followed by all `1`s, and then `2`s.

**Example:**
```python
Input: nums = [2, 0, 2, 1, 1, 0]
Output: [0, 0, 1, 1, 2, 2]
```

### ⚖️ Constraints:
- You must solve it **in-place** (i.e., without using extra space).
- You should aim for **one pass** over the array.

### 🎓 Why This Problem Is Important
This isn't just a test of coding. It evaluates your:
- Ability to use **two pointers** effectively
- Understanding of **low-level sorting techniques**
- Capacity to reason through **edge cases** efficiently

### 🔁 Enter: Dutch National Flag Algorithm
Devised by the legendary computer scientist Edsger W. Dijkstra, this algorithm efficiently partitions an array into three distinct parts.

Here's how it works:
- Use three pointers: `low`, `mid`, and `high`
- Iterate through the list with `mid`
  - If `nums[mid] == 0`: swap with `nums[low]`, increment both `low` and `mid`
  - If `nums[mid] == 1`: just increment `mid`
  - If `nums[mid] == 2`: swap with `nums[high]`, decrement `high`

### 📄 Code Implementation
```python
class Solution:
    def sortColors(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

### 🎮 Dry Run
Given: `[2, 0, 2, 1, 1, 0]`
- Initial: `low = 0`, `mid = 0`, `high = 5`
- Step 1: nums[0] == 2 → swap with nums[5]: [0, 0, 2, 1, 1, 2], high--
- Step 2: nums[0] == 0 → swap with nums[0], low++, mid++
- Step 3: nums[1] == 0 → swap with nums[1], low++, mid++
- Step 4: nums[2] == 2 → swap with nums[4], high--
- Step 5: nums[2] == 1 → mid++
- Step 6: nums[3] == 1 → mid++
Done: `[0, 0, 1, 1, 2, 2]`

### 🚀 Advantages of the Dutch National Flag Algorithm
- **Linear Time Complexity (O(n))**: Perfect for scenarios with a known and limited set of elements (like 0, 1, and 2).
- **In-place Sorting**: No extra space used, memory efficient.
- **One Pass**: It solves the entire problem in just a single traversal of the array.
- **Optimal for Exactly 3 Categories**: Ideal when you're dealing with a classification problem involving three types.

> ❗ Note: This algorithm only works when there are **exactly three distinct elements**. For more than three, you'll need a more general solution like counting sort or a generic sorting algorithm.

### 🎉 Final Thoughts
LeetCode 75 teaches an elegant algorithm that blends theory with practical coding skills. Master this, and you're one step closer to acing those technical interviews!

