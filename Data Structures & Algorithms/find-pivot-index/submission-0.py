class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 1)
        suffix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]

        for i in range(len(nums), 0, -1):
            suffix[i-1] = suffix[i] + nums[i-1]
  
        
        for i in range(len(nums)):
            if prefix[i] == suffix[i+1]:
                return i
        
        return -1
