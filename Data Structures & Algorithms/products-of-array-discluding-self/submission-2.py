import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    
        prefix = [1] * (len(nums) +1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] * nums[i]

        suffix = [1] * (len(nums) +1)
        for i in range(len(nums), 0, -1):
            suffix[i-1] = suffix[i] * nums[i-1]

        res = [0]*len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] *suffix[i+1]

        return res

