class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1,n2=len(word1),len(word2)
        i=j=0
        merge=[]
        while i<n1 and j<n2: 
            merge.append(word1[i])
            merge.append(word2[j])
            i+=1
            j+=1
        merge.extend(word1[i:])
        merge.extend(word2[j:])
        return "".join(merge)
