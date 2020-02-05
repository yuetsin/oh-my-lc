// written by @cl0ud_runner

class Solution {
    func maxCount(_ m: Int, _ n: Int, _ ops: [[Int]]) -> Int {
        var minX = m
        var minY = n
        
        for op in ops {
            minX = min(op[0], minX)
            minY = min(op[1], minY)
        }

        return minX * minY
    }
}