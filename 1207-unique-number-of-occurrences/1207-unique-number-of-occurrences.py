from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = defaultdict(int)

        for num in arr:
            d[num] += 1
        
        counts = d.values()
        if len(counts) == len(set(counts)):
            return True
        return False
        