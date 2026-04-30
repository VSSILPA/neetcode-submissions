class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for index, val in enumerate(arr):
            max = -99999999
            for j in range(index+1, len(arr)):
                if arr[j] > max:
                    max = arr[j]
            arr[index] = max
        arr[-1] = -1
        return arr