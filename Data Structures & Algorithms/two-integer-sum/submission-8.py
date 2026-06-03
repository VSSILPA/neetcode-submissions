class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in lookup:
                return [lookup[complement], i] 
        
            lookup[val] = i
