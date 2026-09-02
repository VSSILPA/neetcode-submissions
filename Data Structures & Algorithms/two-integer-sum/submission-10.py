class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}

        for i in range(len(nums)):
            if target - nums[i] in seen_dict:
                return [seen_dict[target-nums[i]], i]
            seen_dict[nums[i]] = i