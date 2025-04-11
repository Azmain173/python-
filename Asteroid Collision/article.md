**Title:** Crashing Into Clarity: How One Asteroid Problem Made Me a Better Coder

**Header Image:** ![Asteroid Collision Visual](A_high-resolution_digital_photograph_features_the_.png)

---

**Introduction**

It was just another evening of solving LeetCode problems. I stumbled upon **Problem 735: Asteroid Collision** and thought, *"Cool! Physics meets code—should be fun!"* What followed, however, was an emotional rollercoaster of confusion, debugging, frustration, and ultimately, growth.

---

**The Problem That Made Me Pause**

Here's the actual problem statement:

> **LeetCode 735 - Asteroid Collision**
>
> We are given an array `asteroids` of integers representing asteroids in a row. 
> 
> - Each asteroid moves at the same speed.
> - A positive value means it is moving to the right, and a negative value means it is moving to the left.
> - When two asteroids collide, the smaller one explodes.
> - If both are the same size, both explode.
> - Two asteroids moving in the same direction will never meet.
>
> Return an array representing the state of the asteroids after all collisions.

Example:
```python
Input: [5, 10, -5]  Output: [5, 10]
Input: [8, -8]       Output: []
Input: [10, 2, -5]   Output: [10]
Input: [-2, -1, 1, 2] Output: [-2, -1, 1, 2]
```

I wrote this code initially:
```python
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                    break
                else:
                    stack.append(asteroid)

        return stack
```

And then came my confusion: *Why is the `else:` block placed outside the `while`?* I was expecting it to always execute if the loop doesn’t run—but that’s not how Python works.

---

**The "Aha!" Moment**

That's when I realized: in Python, the `else` attached to a loop only runs when the loop is not exited by a `break`. Since my code had `break` statements inside the loop, the `else` was never running as expected.

So I rewrote the logic with a flag variable called `alive` to keep things simple and intuitive:

```python
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            alive = True

            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                    alive = False
                    break
                else:
                    alive = False
                    break

            if alive:
                stack.append(asteroid)

        return stack
```

Now everything clicked. I tested it with different inputs, and it worked beautifully. No surprises. No hidden behavior. Just clean logic.

---

**Complexity Analysis**

- **Time Complexity:** `O(n)` – Each asteroid is pushed and popped from the stack at most once.
- **Space Complexity:** `O(n)` – In the worst case, no collisions occur, and all asteroids are stored.

---

**Why This Matters**

It wasn’t just about solving a LeetCode problem. It was a lesson in how deeply understanding your tools—like Python syntax—can be the difference between a bug hunt and elegant code.

More importantly, it reminded me that the journey to clarity often involves crashing through confusion. Just like the asteroids in the problem, I had to go through my own collisions with code.

---

**Takeaways**

- Don’t underestimate the quirks of your programming language.
- It’s okay to be confused—what matters is pushing through.
- Debugging is not a sign of failure; it's the path to mastery.

---

**Want to Try It Yourself?**
Check out the full code, explanation, complexity analysis, and sample test cases in my [GitHub repo](#) (or message me—I’ll happily share!)

And if you ever feel like giving up on a problem, remember: sometimes you need to crash to learn how to fly 🚀

---

**#leetcode #python #growthstory #debugging #learnbydoing #storytime**

