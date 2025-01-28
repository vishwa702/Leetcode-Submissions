class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        
        n1 = len(word1)
        n2 = len(word2)
        maxlen = max(n1, n2)
        
        i, j = 0, 0
    
        while i < maxlen or j < maxlen:
            if i < n1:
                ans = ans + word1[i]
            
            if j < n2:
                ans = ans + word2[j]

            i += 1
            j += 1
        
        return ans
