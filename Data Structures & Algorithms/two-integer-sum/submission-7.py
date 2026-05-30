class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i, val in enumerate(nums):
            diff = target-val
            if diff in lookup:
                return [lookup[diff], i]
            else:
                lookup[val] = i