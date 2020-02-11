// written by @Colix

func repeatedStringMatch(A string, B string) int {
	cnt := int(math.Ceil(float64(len(B)) / float64(len(A))))
	rpt := strings.Repeat(A, cnt)
	if strings.Contains(rpt, B) {
		return cnt
	}
	if strings.Contains(rpt+A, B) {
		return cnt + 1
	}
	return -1
}