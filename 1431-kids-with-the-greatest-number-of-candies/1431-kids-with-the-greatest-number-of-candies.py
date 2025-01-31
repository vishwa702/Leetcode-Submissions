class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if num + extraCandies >= max(candies) else False for num in candies] 