func findPoisonedDuration(timeSeries []int, duration int) int {
	rst := 0

	if len(timeSeries) == 0 {
		return rst
	}

	poisonedMax := timeSeries[0] // 设置最新中毒坐标
	for k, v := range timeSeries {
		if poisonedMax > v {
			rst += v - timeSeries[k-1] // 累加的长度是前两个元素的间隔
		} else {
			rst += duration
		}
		poisonedMax = v + duration
	}
	return rst
}