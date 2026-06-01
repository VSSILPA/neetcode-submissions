import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [0] * len(nums)
        for i, val in enumerate(nums):
            product = math.prod(nums[0:i] + nums[i+1:])
            prod[i] = product

        return prod
        