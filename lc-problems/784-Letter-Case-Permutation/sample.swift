// written by @user2305M

class Solution {
    var S: [Character] = []
    func letterCasePermutation(_ S: String) -> [String] {
        var res: [String] = []
        self.S = Array(S)
        helper(0, "", &res)
        return res
    }
    
    func helper(_ i: Int, _ path: String, _ res: inout [String]) {
        guard i <= S.count - 1 else { 
            res.append(path)
            return 
        }
        
        let curr = S[i]
        if curr.isLetter == true {
            helper(i + 1, path + String(curr.lowercased()), &res)
            helper(i + 1, path + String(curr.uppercased()), &res)
        } else {
            helper(i + 1, path + String(curr), &res)
        }
    }
}