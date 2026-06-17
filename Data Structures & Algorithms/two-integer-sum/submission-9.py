
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counter = {}
        for i, n in enumerate(nums):
            if target-n in counter:
                return [counter[target-n], i]
            counter[n] = i
       