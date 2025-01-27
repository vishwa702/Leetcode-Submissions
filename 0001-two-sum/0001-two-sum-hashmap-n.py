class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hash map to store the value and its index
        seen = {}
        
        # Iterate through the list
        for i, num in enumerate(nums):
            # Calculate the complement that would sum to the target
            complement = target - num
            
            # Check if the complement is already in the hash map
            if complement in seen:
                # Return the indices of the current number and the complement
                return [seen[complement], i]
            
            # Store the current number with its index in the hash map
            seen[num] = i

        
        
        
