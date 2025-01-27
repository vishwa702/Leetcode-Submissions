class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        nums_og = nums.copy()
        nums.sort()
        for i in range(n):
            j = i + 1
            while j < n and nums[i] + nums[j] <= target :
                if nums[i] + nums[j] == target:
                    if nums[i] != nums[j]:
                        return (nums_og.index(nums[i]), nums_og.index(nums[j]))
                    else:
                        ans1 = nums_og.index(nums[i])
                        ans2 = nums_og.index(nums[j], ans1 + 1)
                        return (ans1, ans2)
                j += 1

        
        
        
