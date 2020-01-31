class Solution {
    var count = 0
    func countArrangement(_ N: Int) -> Int {
        var used = Array(repeating: false, count: N + 1)
        helper(N, 1, &used)
        return count
    }
    
    func helper(_ N: Int, _ index:Int, _ used:inout [Bool]) {
        if index > N { 
            count += 1
            return
        }
        for i in 1...N {
            if used[i] == true { continue }
            if index % i == 0 || i % index == 0 {
                used[i] = true
                helper(N, index + 1, &used)
                used[i] = false
            }
        }
    }
}