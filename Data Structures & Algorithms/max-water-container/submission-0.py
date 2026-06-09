class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L=0
        R=len(heights)-1
        area=0
        while L<R:
            w = R-L
            h = min(heights[L], heights[R])
            area = max(area, w*h)
            if heights[L] > heights[R]:
                R-=1
            else:
                L+=1

        return area
        