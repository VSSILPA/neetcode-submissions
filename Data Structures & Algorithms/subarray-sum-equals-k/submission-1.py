class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_dict = {0:1}
        current_prefix_sum = 0
        count = 0
        for n in nums:
            current_prefix_sum += n
            needed = current_prefix_sum - k
            if needed in prefix_dict:
                count += prefix_dict[needed] 
            
            prefix_dict[current_prefix_sum] = prefix_dict.get(current_prefix_sum, 0) + 1
        return count