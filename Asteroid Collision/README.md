# Asteroid Collision Problem - Explained

## Question:
**Why is the `else:` placed after the `while` loop? And how is it connected to the `while`?**

## Answer:
In Python, a `while` (or `for`) loop can have an `else` block. The `else` block executes only if the loop
finishes normally (i.e., it is not terminated by a `break` statement). In the asteroid collision problem,
this is useful because we want to add the current asteroid to the stack only if it wasn't destroyed in a collision
(i.e., the `while` loop didn’t break).

However, to make it more beginner-friendly and avoid this lesser-known behavior,
we can rewrite the solution using a **flag variable** instead of the `while...else` structure.

---

## 💡 Problem Description:
You're given a list of integers representing asteroids in a row.

- Each asteroid moves at the same speed.
- A positive integer represents an asteroid moving to the right.
- A negative integer represents an asteroid moving to the left.
- When two asteroids meet, the smaller one explodes. If they are the same size, both explode.
- Two asteroids moving in the same direction never meet.

Return the state of the asteroids after all collisions.

---

## ✅ Rewritten Solution (No `while...else`) with Explanation
```python
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []  # This will keep track of the surviving asteroids

        for asteroid in asteroids:
            alive = True  # Assume the current asteroid is alive/surviving

            # Check for collision: right-moving asteroid (stack[-1] > 0) meets left-moving asteroid (asteroid < 0)
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    # Top of stack is smaller; it explodes, pop it and continue checking
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    # Both are the same size; both explode
                    stack.pop()
                    alive = False  # Current asteroid also gets destroyed
                    break
                else:
                    # The current asteroid is smaller; it explodes
                    alive = False
                    break

            # If the asteroid survived all collisions, push it to the stack
            if alive:
                stack.append(asteroid)

        return stack
```

---

## 🧠 Code Explanation:
- **stack** keeps track of the asteroids that are currently in space.
- **alive** flag determines if the current asteroid survives the collision.
- The **while loop** runs as long as there's a potential for collision (i.e., last in stack is moving right and current is moving left).
- We compare magnitudes and pop/destroy asteroids accordingly.

---

## 🧪 Example Usage:
```python
sol = Solution()
print(sol.asteroidCollision([5, 10, -5]))   # Output: [5, 10]
print(sol.asteroidCollision([8, -8]))       # Output: []
print(sol.asteroidCollision([10, 2, -5]))   # Output: [10]
print(sol.asteroidCollision([-2, -1, 1, 2]))# Output: [-2, -1, 1, 2]
```

---

## ⏱️ Time and Space Complexity:
- **Time Complexity:** `O(n)` where `n` is the number of asteroids. Each asteroid is pushed and popped at most once.
- **Space Complexity:** `O(n)` in the worst case, when no collisions happen and all asteroids are added to the stack.

---

## 📘 Summary:
- The original `while...else` form is Pythonic but can be hard to understand.
- Using a flag like `alive` makes it clearer for beginners.
- This solution efficiently handles all cases and is easy to follow.

Let me know if you'd like this exported as a `README.md` file for GitHub, or want visuals added!
