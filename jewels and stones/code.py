class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        h=set(jewels)
        for stone in stones:
            if stone in h:
                count+=1
        return count
