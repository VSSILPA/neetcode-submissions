import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [0]*len(nums)
        suffix[0] = 1
        for i in range(1, len(nums)):
            suffix[i] = suffix[i-1] * nums[i-1]

        prefix =[0]*len(nums)
        prefix[len(nums)-1] =1

        for i in range(len(nums)-2, -1, -1):
            prefix[i] = prefix[i+1] * nums[i+1]
        
        res = []
        for i in range(len(nums)):
            res.append(suffix[i] * prefix[i])

        return(res)
