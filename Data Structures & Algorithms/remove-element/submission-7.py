class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for index, num in enumerate(nums):
            if num != val:
                count = count + 1
            else:
                for non_val_idx in range(index, len(nums)):
                    if nums[non_val_idx] != val:
                        nums[index] = nums[non_val_idx]
                        nums[non_val_idx] = num
                        count = count + 1
                        break
        return count
