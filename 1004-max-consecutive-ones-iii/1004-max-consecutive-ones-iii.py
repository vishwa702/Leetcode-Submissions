class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l ,count_zeros, max_span = 0, 0, 0

        for r in range(len(nums)):


            if nums[r] == 0:
                count_zeros += 1

            while count_zeros > k:

                if nums[l] == 0:
                    count_zeros -= 1
                l += 1

            max_span = max(max_span, r - l + 1)

        return max_span
