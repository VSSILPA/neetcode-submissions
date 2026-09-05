class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1

        while left < right:
            curr = numbers[left] + numbers[right]
            if curr <  target:
                left += 1
            elif curr > target:
                right -=1
            elif curr == target:
                return [left+1, right+1]






# [-1,2,3,4, 5] target =7 target 1,4

# [-5, 1], target = 6, target 1,2t =0