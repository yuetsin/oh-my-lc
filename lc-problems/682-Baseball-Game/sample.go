// written by @Colix

func calPoints(ops []string) (sum int) {
	points := make([]int, len(ops))
	for _, op := range ops {
		switch op {
		case "+":
			points = append(points, points[len(points)-1]+points[len(points)-2])
		case "D":
			points = append(points, 2*points[len(points)-1])
		case "C":
			points = points[:len(points)-1]
		default:
			point, _ := strconv.Atoi(op)
			points = append(points, point)
		}
	}
	for _, point := range points {
		sum += point
	}
	return
}