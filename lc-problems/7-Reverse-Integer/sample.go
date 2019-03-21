func reverse(x int) int {
    sign := 1
    if x < 0{
        sign = -1
        x = x * -1
    }
    result := 0
    for x > 0{
        result = result * 10 + x % 10
        if result > math.MaxInt32{
            return 0
        }
        x = x/10
    }
    return sign * result
}