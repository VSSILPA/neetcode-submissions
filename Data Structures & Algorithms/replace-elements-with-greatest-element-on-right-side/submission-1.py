class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # initial max = -1
        # reverse iteration
        
        rightmax = -1

        for i in range(len(arr)-1,-1,-1):
            new_max = max(rightmax, arr[i])
            arr[i] = rightmax
            rightmax = new_max
        return arr