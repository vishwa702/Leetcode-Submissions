class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Iterate through the list while checking if previous and next elements are 0. If yes, change the current element in place. 

        if n == 0:
            return True

        l = len(flowerbed)

        count_placable = 0
        
        i = 0
        while i < l: 
            if flowerbed[i] == 0:
                if ( i == 0 or flowerbed[i-1] == 0) and (i == l-1 or flowerbed[i+1] == 0):
                    flowerbed[i] = 1
                    count_placable += 1

                    if count_placable >= n : return True
            
            i += 1


        
        return count_placable >= n

