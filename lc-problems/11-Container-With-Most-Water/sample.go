func maxArea(height []int) int {
	var start, end, maxArea, tmpArea int
	end = len(height) - 1
    if end == 1 {
        if height[0] < height[1] { return height[0] }
		return height[1]
	}
	for start < end {
		if height[start] < height[end] {
			tmpArea = height[start] * (end - start)
			start++
		} else {
			tmpArea = height[end] * (end - start)
			end--
		}
		if tmpArea > maxArea { maxArea = tmpArea }
	}
	return maxArea
}