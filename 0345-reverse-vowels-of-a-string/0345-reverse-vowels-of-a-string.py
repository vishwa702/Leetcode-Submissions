class Solution:
    def reverseVowels(self, s: str) -> str:
        size = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        l, r = 0, size - 1
    
        s = list(s)

        while True:

            # push l to the next vowel
            while l < size and not s[l] in vowels:
                l += 1
            
            # push r to the next vowel
            while r >= 0 and not s[r] in vowels:
                r -= 1


            # print(f'Swapping s[{l}]: {s[l]} and s[{r}]: {s[r]} ')

            if l >= r:
                break

            # swap chars at l and r
            s[l], s[r] = s[r], s[l]

            # Push both l and r by 1 step
            l += 1
            r -= 1

        return ''.join(s)