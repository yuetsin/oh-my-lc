class Solution {
    func reverse(_ x: Int) -> Int {
        guard x <= (2<<30 - 1) && x >= -(2<<30) else {return 0}
        var sum = 0
        var absX = abs(x)
        while absX > 0 {
            sum *= 10
            sum += absX % 10
            absX /= 10
        }
        if sum <= (2<<30 - 1) && sum >= -(2<<30) { return x > 0 ? sum : -sum}
        else {return 0}
    }
}