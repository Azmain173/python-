from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
    
        for asteroid in asteroids:
            alive = True  # assume the asteroid survives
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()  # right asteroid is smaller and explodes
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()  # both explode
                    alive = False
                    break
                else:
                    # left-moving asteroid is smaller and explodes
                    alive = False
                    break
            if alive:
                stack.append(asteroid)
        
        return stack
