class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        left=0
        right=price[-1]-price[0]

        while left<right:
            mid=left+(right-left)//2
            count=1
            last=price[0]

            for p in price[1:]:
                if p-last>=mid:
                    count+=1
                    last=p

            if count>=k:
                left=mid+1
        
        
            else:
                right=mid-1

        return left-1
