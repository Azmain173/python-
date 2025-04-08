class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n=len(people)
        people.sort()
        l=0
        r=n-1
        boat=0
        while l<=r:
            if people[l]+people[r]<=limit:
                l+=1
            r-=1
            boat+=1
        return boat

        
