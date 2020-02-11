// written by @followben

class Solution {
    
    var dp: [[Int]: Double] = [:]

    func knightProbability(_ N: Int, _ K: Int, _ r: Int, _ c: Int) -> Double {
        guard r >= 0 && r < N && c >= 0 && c < N else {
            return 0
        }
        guard K > 0 else {
            return 1
        }
        let key: [Int] = [r,c,K]
        if let result = dp[key] {
            return result
        }
        let total = knightProbability(N, K - 1, r - 1, c - 2) +
                knightProbability(N, K - 1, r - 2, c - 1) +
                knightProbability(N, K - 1, r - 1, c + 2) +
                knightProbability(N, K - 1, r - 2, c + 1) +
                knightProbability(N, K - 1, r + 1, c + 2) +
                knightProbability(N, K - 1, r + 2, c + 1) +
                knightProbability(N, K - 1, r + 1, c - 2) +
                knightProbability(N, K - 1, r + 2, c - 1)
        let result = total / 8
        dp[key] = result
        return result
    }
}