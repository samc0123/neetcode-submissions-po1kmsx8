class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 
        for l in range(len(heights)):
            l_height = heights[l]
            for r in range(l+1, len(heights), 1):
                r_height = heights[r]
                area = min(l_height,r_height) * (r-l)

                max_area = max(max_area,area)

        return max_area