**Summary of Key Questions in the Three Sum Problem**

### 1. **Why `len(nums) - 2` in the loop condition?**
   - Since we are looking for triplets (`i, left, right`), we need at least **three numbers** in our search.
   - `left` is always `i + 1` and `right` is `len(nums) - 1`, so stopping at `len(nums) - 2` ensures `left` and `right` always have valid indices.

### 2. **Why do we check `if i > 0 and nums[i] == nums[i - 1]`?**
   - This is to **skip duplicate values for `i`** to avoid generating the same triplets multiple times.
   - If `i == 0`, there’s no `i-1`, so we need `i > 0` before comparing `nums[i]` with `nums[i-1]`.

### 3. **Why not just `i+1` instead of `continue` to skip duplicates?**
   - If we don’t use `continue`, the loop still runs for duplicate `i`, leading to duplicate triplets.
   - `continue` skips the rest of the loop body and moves `i` forward without checking duplicate cases.

### 4. **Why do we move `left` and `right` when `total < 0` or `total > 0`?**
   - Since `nums` is sorted:
     - If `total < 0`, increasing `left` moves to a larger value, pushing `total` towards `0`.
     - If `total > 0`, decreasing `right` moves to a smaller value, reducing `total` to `0`.

### 5. **Why do we skip duplicates for `left` and `right`?**
   - If `nums[left]` is the same as `nums[left+1]`, moving `left` forward ensures we don’t reuse the same value for multiple triplets.
   - Similarly, if `nums[right]` is the same as `nums[right-1]`, moving `right` backward ensures uniqueness.

### 6. **Why is there a final `left += 1` and `right -= 1` after finding a valid triplet?**
   - Since `nums[i] + nums[left] + nums[right] == 0`, we need to find **new unique pairs**.
   - Moving `left` and `right` helps explore other potential triplets without reusing the same values.

### 7. **Can the code be shortened?**
   - Yes! The logic can be optimized by:
     - Using inline `while` loops for skipping duplicates.
     - Keeping variable names short (`res` instead of `result`).
     - Removing unnecessary comments when logic is clear.

### **Conclusion**
This problem is tricky because it involves handling duplicates **at three different levels** (`i`, `left`, `right`). Understanding how each part contributes to **avoiding duplicates** and **optimizing searches** makes the solution clearer. With practice, this becomes easier to implement!

