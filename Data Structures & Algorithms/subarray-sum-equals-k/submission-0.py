class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        sum = 0
        out =0
        for val in nums:
            sum += val
            diff = sum-k
            out +=  prefix.get(diff, 0)
            prefix[sum] = prefix.get(sum, 0) + 1
        return out
