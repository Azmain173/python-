# 🚤 Leetcode 881 - Boats to Save People

## 🧩 Problem Description

You are given an array `people` where `people[i]` is the weight of the i-th person, and an integer `limit` representing the **maximum weight a boat can carry**.

- Each boat can carry **at most two people** at the same time.
- The sum of their weights must be **less than or equal to** `limit`.
- Return the **minimum number of boats** required to carry everyone.

---

## 🧐 Approach: Two Pointers + Greedy

### ✅ Strategy

1. **Sort** the `people` array.
2. Use two pointers:
   - `i` starts at the **beginning** (lightest person).
   - `j` starts at the **end** (heaviest person).
3. Try to pair the lightest (`people[i]`) with the heaviest (`people[j]`).
   - If they fit within the limit, send both: `i++`, `j--`.
   - Otherwise, send the heavier person alone: `j--`.
4. In either case, **use one boat** and increment the counter.

---

## 🯞 Python Code

```python
def numRescueBoats(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    boats = 0

    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1  # Lightest person boards too
        j -= 1      # Heaviest person always boards
        boats += 1  # One boat used
    return boats
```

---

## ❓ Why the Pointers Are Used Like That

### 🏃 `i += 1` (Lightest Person)
- This happens **only if** the lightest and heaviest can go together.
- Checked using: `if people[i] + people[j] <= limit`

### 🧐 `j -= 1` (Heaviest Person)
- This **always happens** because we always send the heaviest person (alone or paired).

### ⛵ `boats += 1`
- A boat is always used in each loop iteration—either for:
  - One person (if pairing not possible), or
  - Two people (if pairing is possible)

---

## 🧪 Example

```python
people = [3, 2, 2, 1]
limit = 3

# Sorted: [1, 2, 2, 3]

# Boat 1: 1 + 2
# Boat 2: 2 alone
# Boat 3: 3 alone

# Total: 3 boats
```

---

## ⏱️ Time and Space Complexity

- **Time Complexity:** `O(n log n)` due to sorting
- **Space Complexity:** `O(1)` (in-place two-pointer logic)

---

## 🔗 Related Topics
- Greedy
- Two Pointers
- Sorting

---

## 📌 Tip

Always try to send the **heaviest person** first. Pair them with the lightest **only if possible**. This greedy strategy ensures minimal boat usage.

