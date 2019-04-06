class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        possible_value = 0
        tot_width = len(heights)

        lptr = 0
        rptr = tot_width - 1

        while lptr <= rptr:
            current_s = 0
            if lptr == rptr:
                current_s = heights[lptr]
            else:
                current_s = min(heights[lptr: rptr + 1]) * (rptr - lptr + 1)

            if possible_value < current_s:
                possible_value = current_s

            if  # ... Go left or right?...
            lptr += 1
            else:
                rptr -= 1

        return possible_value
